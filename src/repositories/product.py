""" Defines the Product repository """

from models import Product


class ProductRepository:
    """ The repository for the product model """

    @staticmethod
    def get(product_id):
        """ Query a product by last and first name """
        return Product.query.filter_by(id=product_id).one_or_none()

    @staticmethod
    def create(
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
