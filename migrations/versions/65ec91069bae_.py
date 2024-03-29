"""empty message

Revision ID: 65ec91069bae
Revises: b2e5e40f5230
Create Date: 2019-11-21 01:29:14.484154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65ec91069bae'
down_revision = 'b2e5e40f5230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tag_slug_key', 'tag', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tag_slug_key', 'tag', ['slug'])
    # ### end Alembic commands ###
