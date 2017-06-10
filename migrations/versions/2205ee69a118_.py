"""empty message

Revision ID: 2205ee69a118
Revises: 2dc61cab6b58
Create Date: 2017-06-10 11:41:13.701652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2205ee69a118'
down_revision = '2dc61cab6b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search_counter', sa.Column('session_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('search_counter', 'session_count')
    # ### end Alembic commands ###