"""tenth migration

Revision ID: ec2156e0bd1c
Revises: b69735af936c
Create Date: 2019-04-27 13:25:28.794292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec2156e0bd1c'
down_revision = 'b69735af936c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'author')
    # ### end Alembic commands ###
