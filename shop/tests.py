from django.test import TestCase, Client
from shop.views import _get_resource, update_products


class TestAPI(TestCase):
    """
    Test api calls for competition
    """

    def setUp(self):
        self.client = Client()

    def test_api_orders(self):
        response = self.client.get('/api/load/order')
        self.assertEqual(response.json(), {'a':'b'})
        return self.assertEqual(response.status_code, 200)

    def test_get_resource__order(self):
        response = _get_resource('orders')
        self.assertEqual(response[0]['id'], 2300748070979)

    def test_update_products(self):
        result = update_products({})
        return self.assertEqual(result, [])

    def test_decrement_inventory(self):
        self.assertTrue(False)
