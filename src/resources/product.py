
"""
Define the REST verbs relative to the products
"""

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import ProductRepository
from util import parse_params


class ProductResource(Resource):
    """ Verbs relative to the products """

    @staticmethod
    @swag_from('../swagger/product/GET.yml')
    def get(product_id):
        """ Return a product key information based on its id """

        product = ProductRepository.get(product_id)
        return jsonify({
            'product': product.json if product else None
        })


class ProductCreationResource(Resource):

    @staticmethod
    @swag_from('../swagger/product/POST.yml')
    @parse_params(
        Argument('name', location='json', required=True, help='The name of the product.'),
        Argument('brand', location='json', required=True, help='The brand of the product.'),
        Argument('price', location='json', required=True, help='The price of the product.'),
        Argument('category', location='json', required=True, help='The category of the product.'),
        Argument('subcategory', location='json', required=True, help='The subcategory of the product.'),
        Argument('subsubcategory', location='json', required=True, help='The subsubcategory of the product.'),
        Argument('description', location='json', required=False, help='The description of the product.'),
        Argument('image', location='json', required=False, help='The image of the product.'),
        Argument('rating', location='json', required=False, help='The rating of the product.'),
    )
    def post(
        name,
        brand,
        price,
        category,
        subcategory,
        subsubcategory,
        description=None,
        image=None,
        rating=None,
    ):
        """ Create an product based on the sent information """
        product = ProductRepository.create(
            name,
            brand,
            price,
            category,
            subcategory,
            subsubcategory,
            description,
            image,
            rating,
        )
        return jsonify({'product': product.json})
