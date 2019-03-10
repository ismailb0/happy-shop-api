""" Defines the Product repository """

from models import Product


class ProductRepository:
    """ The repository for the product model """

    @staticmethod
    def get(product_id):
        """ Query a product by last and first name """
        return Product.query.filter_by(id=product_id).one_or_none()

    @staticmethod
    def get_all(
        start_price,
        end_price,
        category,
        subcategory,
        subsubcategory,
        sorted,
    ):
        """ Query all products filtered by price, category and sorted """

        product_query = Product.query

        if start_price:
            product_query = product_query.filter(start_price <= Product.price)
        if end_price:
            product_query = product_query.filter(Product.price <= end_price)
        if category:
            product_query = product_query.filter_by(category=category)
        if subcategory:
            product_query = product_query.filter_by(subcategory=subcategory)
        if subsubcategory:
            product_query = product_query.filter_by(subsubcategory=subsubcategory)
        if sorted:
            product_query = product_query.order_by(Product.price.asc())

        return product_query

    @staticmethod
    def create(
        name,
        brand,
        price,
        category,
        subcategory,
        subsubcategory,
        description,
        image=None,
        rating=None,
    ):
        """ Create a new product """
        product = Product(
            name,
            brand,
            price,
            category,
            subcategory,
            subsubcategory,
            description,
            image,
            rating
        )

        return product.save()
