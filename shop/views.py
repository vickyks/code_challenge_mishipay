import json

import requests
from django.db.utils import IntegrityError
from django.http import HttpResponse

from mishipay_app import settings
from shop.models import Order, Product


def _get_resource(resource):
    username = settings.SHOPIFY_API_KEY
    password = settings.SHOPIFY_PASSWORD
    shop_name = settings.SHOPIFY_SHOP_NAME
    api_version = settings.SHOPIFY_API_VERSION
    uri = f'https://{username}:{password}@{shop_name}.myshopify.com/admin/api/{api_version}/{resource}.json'
    response = requests.get(uri)
    return response.json()[resource]


def update_or_create(model, details):
    """
    a bit like Django's update_or_create, except that
    Django's built in update or create only works on querysets
    """

    # align data and fields
    available_fields = set(model._meta.fields)
    aligned_fields = set(details.keys()) & available_fields

    details = {k: v for k, v in details.items() if k in aligned_fields}

    try:
        m, created = model.objects.get_or_create(**details)
    except IntegrityError:
        # definitely exists
        m = model.objects.get(id=details['id'])
        for k, v in details.items():
            if k != 'id':
                setattr(m, k, v)
        m.save()
    return m


def update_products(request):
    orders = _get_resource('orders')
    for o in orders:
        for product in o['line_items']:
            # XXX: should get this from InventoryLevel api
            product.update({'inventory_level': 10})
            update_or_create(Product, product)

    return HttpResponse(json.dumps(list(Product.objects.values_list('id', flat=True))))


def load_orders(request):
    orders = _get_resource('orders')

    for o in orders:
        update_or_create(Order, o)

        for product in o['line_items']:
            p, created = Product.objects.get_or_create(id=product['id'])

            if created:
                p.inventory_level = 0
            else:
                p.inventory_level -= 1

            p.save()

    return HttpResponse(json.dumps(list(Order.objects.values_list('id', flat=True))))
