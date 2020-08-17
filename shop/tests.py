from django.test import TestCase, Client


class TestAPI(TestCase):
    """
    Test api calls for competition
    """

    def setUp(self):
        self.client = Client()

    def test_api_orders(self):
        response = self.client.get('/api/load/order')
        return self.assertEqual(response.status_code, 200)

