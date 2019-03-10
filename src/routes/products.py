"""
Defines the blueprint for the products
"""
from flask import Blueprint
from flask_restful import Api

from resources import ProductListResource

PRODUCT_LIST_BLUEPRINT = Blueprint('products', __name__)
Api(PRODUCT_LIST_BLUEPRINT).add_resource(ProductListResource, '/products')
