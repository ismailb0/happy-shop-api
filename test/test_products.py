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
          description="Lorem ipsum dolor sit amet.",
          units_sold=12
        ).save()
        Product(
          name="My Awesome Product 2",
          brand="My Awesome Brand 2",
          price=52.00,
          category="Makeup",
          subcategory="Face",
          subsubcategory="Tools",
          description="Lorem ipsum dolor sit amet.",
          units_sold=11
        ).save()
        Product(
          name="My Awesome Product 3",
          brand="My Awesome Brand 3",
          price=54.00,
          category="Makeup",
          subcategory="Cheek",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet.",
          units_sold=13
        ).save()
        Product(
          name="My Awesome Product 4",
          brand="My Awesome Brand 4",
          price=56.00,
          category="Makeup",
          subcategory="Cheek",
          subsubcategory="Tools",
          description="Lorem ipsum dolor sit amet.",
          units_sold=22
        ).save()
        Product(
          name="My Awesome Product 5",
          brand="My Awesome Brand 5",
          price=58.00,
          category="Perfume",
          subcategory="Nails",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet.",
          units_sold=37
        ).save()
        Product(
          name="My Awesome Product 6",
          brand="My Awesome Brand 6",
          price=60.00,
          category="Perfume",
          subcategory="Nails",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet.",
          units_sold=1
        ).save()
        Product(
          name="My Awesome Product 7",
          brand="My Awesome Brand 7",
          price=12.00,
          category="TEST_CATEGORY",
          subcategory="TEST_SUB_CATEGORY",
          subsubcategory="TEST_SUB_SUB_CATEGORY",
          description="Lorem ipsum dolor sit amet.",
          units_sold=120
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
              "units_sold": 120,
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
              "units_sold": 37,
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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 12,
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
              "units_sold": 11,
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
              "units_sold": 1,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 7)

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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 12,
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
              "units_sold": 11,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 4)

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
              "units_sold": 12,
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
              "units_sold": 11,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 2)

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
              "units_sold": 37,
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
              "units_sold": 13,
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
              "units_sold": 12,
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
              "units_sold": 1,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 4)

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
              "units_sold": 37,
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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 11,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 4)

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
              "units_sold": 37,
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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 11,
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
              "units_sold": 1,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 5)

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
              "units_sold": 120,
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
              "units_sold": 13,
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
              "units_sold": 12,
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
              "units_sold": 11,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 4)

    def test_get_all_products_with_sorted_by_price(self):
        """ The GET on `/products` should return all products sorted by price """
        response = self.client.get(
            '/application/products?sorted=price',
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
              "units_sold": 120,
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
              "units_sold": 12,
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
              "units_sold": 11,
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
              "units_sold": 13,
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
              "units_sold": 22,
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
              "units_sold": 37,
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
              "units_sold": 1,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 7)

    def test_get_all_products_with_no_filtered_by_multiple_categories(self):
        """ The GET on `/products` should return all products filtered by multiple categories """
        response = self.client.get(
            '/application/products?category=Makeup,Perfume',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        expected = [
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
              "units_sold": 37,
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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 12,
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
              "units_sold": 11,
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
              "units_sold": 1,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 6)

    def test_get_all_first_page_products(self):
        """ The GET on `/products` should return a paginated list of products """
        response = self.client.get(
            '/application/products?page=1&results_per_page=5&pagination=true',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))

        self.maxDiff = None

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
              "units_sold": 120,
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
              "units_sold": 37,
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
              "units_sold": 22,
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
              "units_sold": 13,
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
              "units_sold": 12,
            },
        ]

        self.assertEqual(response_json["products"], expected)
        self.assertEqual(response_json["count"], 7)
