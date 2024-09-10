from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductModelTest(TestCase):
    def setUp(self):
        # create a product
        self.product1 = Product.objects.create(
            name="Gaming Mouse",
            price=100000,
            description="A cheap build-quality gaming mouse",
            category="Mouse",
            stock=10,
            rating=2.7,
        )

        self.product2 = Product.objects.create(
            name="Mechanical Keyboard",
            price=1000000,
            description="A premium mechanical keyboard",
            category="Keyboard",
            stock=5,
            rating=4.8,
        )

    def test_product_creation(self):
        """test if the product that we have created is correct"""
        self.assertEqual(self.product1.name, "Gaming Mouse")
        self.assertEqual(self.product1.price, 100000)
        self.assertEqual(self.product2.category, "Keyboard")

    def test_is_rating_high(self):
        """test if the product has a high rating"""

        # product 2 has a 4.8, so it should have a high rating
        self.assertTrue(self.product2.is_high_rating)

        # product 1 has a 2.7, so it should not have a high rating
        self.assertFalse(self.product1.is_high_rating)

    def test_str_method(self):
        """test the __str__ method of the Product model"""
        self.assertEqual(str(self.product1), "Gaming Mouse")
        self.assertEqual(str(self.product2), "Mechanical Keyboard")