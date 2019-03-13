
"""
Define the REST verbs relative to the products list
"""

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import ProductRepository
from util import parse_params


class ProductListResource(Resource):
    """ Verbs relative to the products """

    @staticmethod
    @swag_from('../swagger/products/GET.yml')
    @parse_params(
        Argument('start_price', location='args', required=False, help='The price to filter products from'),
        Argument('end_price', location='args', required=False, help='The price to filter to'),
        Argument('category', location='args', required=False, help='The category to filter on'),
        Argument('subcategory', location='args', required=False, help='The subcategory to filter on'),
        Argument('subsubcategory', location='args', required=False, help='The subsubcategory to filter on'),
        Argument('pagination', location='args', required=False, help='Should the response be paginated'),
        Argument('page', location='args', required=False, help='Page to get the products from'),
        Argument('results_per_page', location='args', required=False, help='Result per page to display'),
        Argument('sorted', location='args', required=False, help='Should the response be sorted by price or by best selling'),
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
        sorted="best_selling"
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
            total = paginated_products.total
        else:
            products = products.all()
            total = len(products)

        product_list = [product.json for product in products]

        return jsonify({
            "products": product_list,
            "count": total
        })
