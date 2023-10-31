from django.test import TestCase
from reservation.models import MenuItem
from reservation.serializers import MenuItemSerializer


# Create your tests here.
class MenuItemTest(TestCase):

    @classmethod
    def setup(cls):
        cls.menu = MenuItem.objects.create(
            title = "Apple",
            price = "100",
            inventory = "40",
        )

    def test_get_item(self):
        item = MenuItem.objects.create(title="Icecream", price="90", inventory="100")
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Icecream : 90")

    
    def test_getall(self):
       
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(data=queryset, many=True)
        print(self.menu)
        
      