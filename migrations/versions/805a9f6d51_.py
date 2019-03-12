"""Add units_sold column to product table

Revision ID: 805a9f6d51
Revises: 31128e55c76
Create Date: 2019-03-11 23:51:31.255712

"""

# revision identifiers, used by Alembic.
revision = '805a9f6d51'
down_revision = '31128e55c76'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('product', sa.Column('units_sold', sa.Integer(), nullable=False, server_default='0'))

def downgrade():
    op.drop_column('product', 'units_sold')
