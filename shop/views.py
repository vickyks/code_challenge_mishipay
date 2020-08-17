import requests
from django.shortcuts import render
from mishipay_app import settings


def get_resource(resource):
    username = settings.SHOPIFY_API_KEY
    password = settings.SHOPIFY_PASSWORD
    shop_name= settings.SHOPIFY_SHOP_NAME
    api_version=settings.SHOPIFY_API_VERSION
    uri = f'https://{username}:{password}@{shop_name}.myshopify.com/admin/api/{api_version}/{resource}.json'
    response = requests.get(uri)
    return response.json()[resource]


def update_inventory():
    products = get_resource('products')
    for p in product:
        # Don't create model twice if it was already loaded
        try:
            product, created = Product.objects.get_or_create(**p)
        except IntegrityError:
            # definitely exists
            p = Product.objects.get(id=p['id'])
            for k, v in p.items():
                if k != 'id':
                    setattr(m, k, v)
            m.save()


def load_orders(request):

    orders = get_resource('orders')

    order, created = Order.objects.get_or_create(**products)
    if not created:
        order.update()
    return HttpResponse(json.dumps(order))


