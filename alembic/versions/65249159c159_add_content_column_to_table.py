"""add content column to table

Revision ID: 65249159c159
Revises: 310fec657089
Create Date: 2021-11-24 18:30:14.639839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65249159c159'
down_revision = '310fec657089'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
