"""fix relationship 4

Revision ID: eb5921723b0f
Revises: e8e25b5aac0a
Create Date: 2024-05-26 16:04:00.458291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb5921723b0f'
down_revision = 'e8e25b5aac0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('extra_column')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('extra_column', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###