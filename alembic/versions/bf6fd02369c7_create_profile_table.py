"""create profile table

Revision ID: bf6fd02369c7
Revises: 7c55f61da761
Create Date: 2025-08-10 04:08:13.854916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf6fd02369c7'
down_revision: Union[str, Sequence[str], None] = '7c55f61da761'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('profiles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(length=100), nullable=True),
                    sa.Column('last_name', sa.String(length=100), nullable=True),
                    sa.Column('bio', sa.String(length=500), nullable=True),
                    sa.Column('avatar_url', sa.String(length=255), nullable=True),
                    sa.Column('phone_number', sa.String(length=20), nullable=True),
                    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('user_id')  # This ensures one-to-one relationship
                    )
    op.create_index(op.f('ix_profiles_id'), 'profiles', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_profiles_id'), table_name='profiles')
    op.drop_table('profiles')
