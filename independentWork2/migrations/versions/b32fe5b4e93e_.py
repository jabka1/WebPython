"""empty message

Revision ID: b32fe5b4e93e
Revises: 3890087d3aa1
Create Date: 2023-12-19 11:10:09.482900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32fe5b4e93e'
down_revision = '3890087d3aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('faculty', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('faculty')

    # ### end Alembic commands ###
