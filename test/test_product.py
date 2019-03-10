import unittest
import json

from server import server
from models.abc import db
from models import Product


class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()
        Product(
          name="Lock-it Foundation",
          brand="KAT VON D",
          price=56.00,
          category="Makeup",
          subcategory="Face",
          subsubcategory="Foundation",
          description="Lorem ipsum dolor sit amet."
        ).save()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/product/1` should return the product with id = 1 """
        response = self.client.get(
            '/application/product/1',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertDictEqual(response_json, {
            "product": {
              "name": "Lock-it Foundation",
              "brand": "KAT VON D",
              "price": 56.00,
              "image": None,
              "rating": None,
              "category": "Makeup",
              "subcategory": "Face",
              "subsubcategory": "Foundation",
              "description": "Lorem ipsum dolor sit amet.",
              "id": 1
            },
        })

    def test_create(self):
        """ The POST on `/product` should create a product """
        response = self.client.post(
            '/application/product',
            content_type='application/json',
            data=json.dumps({
              "name": "My Make Up Product",
              "brand": "My Make Up Brand",
              "price": 76.00,
              "category": "Makeup",
              "subcategory": "Nails",
              "subsubcategory": "Foundation",
              "description": "My product description."
            })
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.maxDiff = None
        self.assertDictEqual(
            response_json, {
                "product": {
                  "name": "My Make Up Product",
                  "brand": "My Make Up Brand",
                  "price": 76.00,
                  "category": "Makeup",
                  "subcategory": "Nails",
                  "id": 2,
                  "image": None,
                  "rating": None,
                  "subsubcategory": "Foundation",
                  "description": "My product description."
                 }
            }
        )
        self.assertEqual(Product.query.count(), 2)
