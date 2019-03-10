import unittest
import json

from server import server
from models.abc import db
from models import Product


class TestProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()
        Product(
          name="My Awesome Product 1",
          brand="My Awesome Brand 1",
          price=50.00,
          category="Makeup",
          subcategory="Face",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 2",
          brand="My Awesome Brand 2",
          price=52.00,
          category="Makeup",
          subcategory="Face",
          subsubcategory="Tools",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 3",
          brand="My Awesome Brand 3",
          price=54.00,
          category="Makeup",
          subcategory="Cheek",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 4",
          brand="My Awesome Brand 4",
          price=56.00,
          category="Makeup",
          subcategory="Cheek",
          subsubcategory="Tools",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 5",
          brand="My Awesome Brand 5",
          price=58.00,
          category="Perfume",
          subcategory="Nails",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 6",
          brand="My Awesome Brand 6",
          price=60.00,
          category="Perfume",
          subcategory="Nails",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet."
        ).save()
        Product(
          name="My Awesome Product 7",
          brand="My Awesome Brand 7",
          price=12.00,
          category="TEST_CATEGORY",
          subcategory="TEST_SUB_CATEGORY",
          subsubcategory="TEST_SUB_SUB_CATEGORY",
          description="Lorem ipsum dolor sit amet."
        ).save()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_products_with_no_filter_no_sort(self):
        """ The GET on `/products` should return all products """
        response = self.client.get(
            '/application/products',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 6,
              "name": "My Awesome Product 6",
              "brand": "My Awesome Brand 6",
              "price": 60.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 7,
              "name": "My Awesome Product 7",
              "brand": "My Awesome Brand 7",
              "price": 12.00,
              "category": "TEST_CATEGORY",
              "subcategory": "TEST_SUB_CATEGORY",
              "subsubcategory": "TEST_SUB_SUB_CATEGORY",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_filtered_by_category(self):
        """ The GET on `/products` should return all products with matching category """
        response = self.client.get(
            '/application/products?category=Makeup',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_filtered_by_subcategory(self):
        """ The GET on `/products` should return all products with matching subcategory """
        response = self.client.get(
            '/application/products?subcategory=Face',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_filtered_by_subsubcategory(self):
        """ The GET on `/products` should return all products with matching subsubcategory """
        response = self.client.get(
            '/application/products?subsubcategory=Foundation',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 6,
              "name": "My Awesome Product 6",
              "brand": "My Awesome Brand 6",
              "price": 60.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_filtered_by_start_price_and_end_price(self):
        """ The GET on `/products` should return all products with matching price """
        response = self.client.get(
            '/application/products?start_price=52&end_price=58',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_filtered_by_start_price(self):
        """ The GET on `/products` should return all products with matching price """
        response = self.client.get(
            '/application/products?start_price=52',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 6,
              "name": "My Awesome Product 6",
              "brand": "My Awesome Brand 6",
              "price": 60.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

    def test_get_all_products_filtered_by_end_price(self):
        """ The GET on `/products` should return all products with matching price """
        response = self.client.get(
            '/application/products?end_price=54',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 7,
              "name": "My Awesome Product 7",
              "brand": "My Awesome Brand 7",
              "price": 12.00,
              "category": "TEST_CATEGORY",
              "subcategory": "TEST_SUB_CATEGORY",
              "subsubcategory": "TEST_SUB_SUB_CATEGORY",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

    def test_get_all_products_with_sorted_by_price(self):
        """ The GET on `/products` should return all products sorted by price """
        response = self.client.get(
            '/application/products?sorted=true',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
            {
              "id": 7,
              "name": "My Awesome Product 7",
              "brand": "My Awesome Brand 7",
              "price": 12.00,
              "category": "TEST_CATEGORY",
              "subcategory": "TEST_SUB_CATEGORY",
              "subsubcategory": "TEST_SUB_SUB_CATEGORY",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 6,
              "name": "My Awesome Product 6",
              "brand": "My Awesome Brand 6",
              "price": 60.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)

    def test_get_all_products_with_no_filtered_by_multiple_categories(self):
        """ The GET on `/products` should return all products filtered by multiple categories """
        response = self.client.get(
            '/application/products?category=Makeup,Perfume',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        self.maxDiff = None

        expected = [
            {
              "id": 1,
              "name": "My Awesome Product 1",
              "brand": "My Awesome Brand 1",
              "price": 50.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 2,
              "name": "My Awesome Product 2",
              "brand": "My Awesome Brand 2",
              "price": 52.00,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 3,
              "name": "My Awesome Product 3",
              "brand": "My Awesome Brand 3",
              "price": 54.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 4,
              "name": "My Awesome Product 4",
              "brand": "My Awesome Brand 4",
              "price": 56.00,
              "category": "Makeup",
              "subcategory": "Cheek",
              "subsubcategory": "Tools",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 5,
              "name": "My Awesome Product 5",
              "brand": "My Awesome Brand 5",
              "price": 58.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            },
            {
              "id": 6,
              "name": "My Awesome Product 6",
              "brand": "My Awesome Brand 6",
              "price": 60.00,
              "category": "Perfume",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "image": None,
              "rating": None,
            }
        ]

        self.assertEqual(response_json, expected)
