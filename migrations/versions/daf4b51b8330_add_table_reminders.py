"""Add table reminders

Revision ID: daf4b51b8330
Revises: 49c7263e04a8
Create Date: 2016-12-13 22:27:25.812801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daf4b51b8330'
down_revision = '49c7263e04a8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reminders',
        sa.Column('id', sa.String(length=45), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=True),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.Column('text', sa.Text(), nullable=False))

def downgrade():
    op.drop_table('reminbers')
