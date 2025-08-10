"""add created_at to users

Revision ID: dca67e7b0b14
Revises: 22813cfbb76d
Create Date: 2025-07-25 04:47:12.728597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dca67e7b0b14'
down_revision: Union[str, Sequence[str], None] = '22813cfbb76d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.alter_column("users", "email", type_=sa.String(255), nullable=False)
    op.create_unique_constraint("uq_users_email", "users", ["email"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "created_at")

