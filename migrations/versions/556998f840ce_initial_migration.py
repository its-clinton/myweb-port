"""Initial migration.

Revision ID: 556998f840ce
Revises: 
Create Date: 2023-05-28 18:52:55.317022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '556998f840ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_image', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_image')

    # ### end Alembic commands ###
