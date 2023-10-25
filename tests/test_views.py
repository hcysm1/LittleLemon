from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):

        MenuItem.objects.create(title="guava", price=10.4, inventory=10)
        MenuItem.objects.create(title="lemon", price=4.5, inventory=12)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(response.status_code, 200)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
