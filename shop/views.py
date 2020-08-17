from django.shortcuts import render

# Create your views here.
def get_product(request):
    """
    Get product information from inventory
    """
    inventory = session.get('inventory')
    return HttpResponse(json.dumps(inventory))


def create_order(request):

    products = get_products

    order, created = Order.objects.get_or_create(**products)
    if not created:
        order.update()

    return HttpResponse(json.dumps(order))

