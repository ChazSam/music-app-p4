"""fix relationship 3

Revision ID: e8e25b5aac0a
Revises: 4efc24173fb5
Create Date: 2024-05-26 15:49:01.866395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8e25b5aac0a'
down_revision = '4efc24173fb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('extra_column', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('extra_column')

    # ### end Alembic commands ###
