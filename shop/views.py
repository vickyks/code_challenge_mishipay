import requests
from django.shortcuts import render
from mishipay_app import settings
from shop.models import Order, Product
from django.db.utils import IntegrityError


def _get_resource(resource):
    username = settings.SHOPIFY_API_KEY
    password = settings.SHOPIFY_PASSWORD
    shop_name= settings.SHOPIFY_SHOP_NAME
    api_version=settings.SHOPIFY_API_VERSION
    uri = f'https://{username}:{password}@{shop_name}.myshopify.com/admin/api/{api_version}/{resource}.json'
    response = requests.get(uri)
    return response.json()[resource]


def update_or_create(model, details):
    # Django's built in update or create only works on querysets
    try:
        m, created = model.objects.get_or_create(**details)
    except IntegrityError:
        # definitely exists
        m = model.objects.get(id=details['id'])
        for k, v in items.details():
            if k != 'id':
                setattr(m, k, v)
        m.save()
    return m


def load_orders(request):

    orders = _get_resource('orders')

    for o in orders:
        update_or_create(Order, o)

        for product in o['line_items']:
            procuct = Product.objects.get(product['id'])
            product.inventory_level -=1
            product.save()

    return HttpResponse(json.dumps(list(Order.objects.values_list('id', flat=True))))


