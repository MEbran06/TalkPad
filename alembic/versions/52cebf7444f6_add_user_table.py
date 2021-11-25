"""add user table

Revision ID: 52cebf7444f6
Revises: 65249159c159
Create Date: 2021-11-24 18:47:11.605365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52cebf7444f6'
down_revision = '65249159c159'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
