
"""
Define the REST verbs relative to the products list
"""

from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import ProductRepository
from util import parse_params


class ProductListResource(Resource):
    """ Verbs relative to the products """

    @staticmethod
    @parse_params(
        Argument('start_price', location='json', required=False, help='The price to filter from'),
        Argument('end_price', location='json', required=False, help='The price to filter to'),
        Argument('category', location='json', required=False, help='The category to filter on'),
        Argument('subcategory', location='json', required=False, help='The subcategory to filter on'),
        Argument('subsubcategory', location='json', required=False, help='The subsubcategory to filter on'),
        Argument('pagination', location='json', required=False, help='Should the response be paginated'),
        Argument('page', location='json', required=False, help='Page to get the products from'),
        Argument('results_per_page', location='json', required=False, help='Result per page to display'),
        Argument('sorted', location='json', required=False, help='Should the response be sorted by price'),
    )
    def get(
        start_price=None,
        end_price=None,
        category=None,
        subcategory=None,
        subsubcategory=None,
        pagination=True,
        page=1,
        results_per_page=10,
        sorted=False
    ):
        """
            Return all products filtered by:
            - Price
            - Category, subcategory or subsubcategory
            Products can also be paginated and sorted by price
        """

        products = ProductRepository.get_all(
            start_price,
            end_price,
            category,
            subcategory,
            subsubcategory,
            sorted,
        )

        if pagination:
            paginated_products = products.paginate(int(page), int(results_per_page), False)
            products = paginated_products.items
        else:
            products = products.all()

        product_list = [product.json for product in products]

        return jsonify(product_list)
