"""Add table of browse_volumes

Revision ID: 49c7263e04a8
Revises: 1fa7e17da8cc
Create Date: 2016-12-11 02:04:44.033621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49c7263e04a8'
down_revision = '1fa7e17da8cc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('browse_volumes',
        sa.Column('id', sa.String(length=45), nullable=False),
        sa.Column('home_view_total', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('browse_volumes')
