"""updated user

Revision ID: 2490ee421cbf
Revises: f86fa8d5d7df
Create Date: 2024-04-20 16:56:06.401241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2490ee421cbf'
down_revision = 'f86fa8d5d7df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.drop_column('specialty')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('birthdate', sa.DateTime(), nullable=False))
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('sex',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('bio',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_column('age')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.INTEGER(), nullable=True))
        batch_op.alter_column('bio',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('sex',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('birthdate')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('specialty', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
