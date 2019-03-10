"""Create Product table

Revision ID: 31128e55c76
Revises: 4f2e2c180af
Create Date: 2019-03-10 13:14:58.731246

"""

# revision identifiers, used by Alembic.
revision = '31128e55c76'
down_revision = '4f2e2c180af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('brand', sa.String(length=300), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('image', sa.String(length=300), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('category', sa.String(length=300), nullable=False),
    sa.Column('subcategory', sa.String(length=300), nullable=False),
    sa.Column('subsubcategory', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('product')
