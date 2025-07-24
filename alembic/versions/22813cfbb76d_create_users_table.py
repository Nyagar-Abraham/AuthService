"""create users table

Revision ID: 22813cfbb76d
Revises: 
Create Date: 2025-07-24 17:37:25.931757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22813cfbb76d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False),
        sa.Column('role', sa.String(255), nullable=False ,default='user'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
