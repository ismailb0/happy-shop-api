"""
Defines the blueprint for the products
"""
from flask import Blueprint
from flask_restful import Api

from resources import ProductResource, ProductCreationResource


PRODUCT_BLUEPRINT = Blueprint('product', __name__)
Api(PRODUCT_BLUEPRINT).add_resource(ProductResource, '/product/<int:product_id>')
Api(PRODUCT_BLUEPRINT).add_resource(ProductCreationResource, '/product')
