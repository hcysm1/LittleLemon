from django.test import TestCase
from restaurant.models import MenuItem


#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        MenuItem.objects.create(title="orange", price=80, inventory=100)
        retrieved_item = MenuItem.objects.get(title="orange")
        self.assertEqual(retrieved_item.title, "orange")

    