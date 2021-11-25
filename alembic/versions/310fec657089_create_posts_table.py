"""create posts table

Revision ID: 310fec657089
Revises: 
Create Date: 2021-11-24 17:11:41.418379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310fec657089'
down_revision = None
branch_labels = None
depends_on = None

#handles the changes
def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False),)
    pass


#handles rolling back those changes
def downgrade():
    op.drop_table('posts')
    pass
