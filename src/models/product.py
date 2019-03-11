"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Product(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product model """
    __tablename__ = 'product'

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    brand = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1500), nullable=True)
    image = db.Column(db.String(300), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    category = db.Column(db.String(300), nullable=False)
    subcategory = db.Column(db.String(300), nullable=False)
    subsubcategory = db.Column(db.String(300), nullable=False)

    def __init__(
        self,
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
        """ Create a new Product """
        self.name = name
        self.brand = brand
        self.price = price
        self.description = description
        self.image = image
        self.rating = rating
        self.category = category
        self.subcategory = subcategory
        self.subsubcategory = subsubcategory
