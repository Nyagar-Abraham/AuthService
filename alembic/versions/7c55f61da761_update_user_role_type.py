"""update user role type

Revision ID: 7c55f61da761
Revises: dca67e7b0b14
Create Date: 2025-07-28 04:11:27.862967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from models import Role


# revision identifiers, used by Alembic.
revision: str = '7c55f61da761'
down_revision: Union[str, Sequence[str], None] = 'dca67e7b0b14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    # # 1. Create the ENUM type
    # role_enum = sa.Enum(Role, name="role")
    # role_enum.create(op.get_bind(), checkfirst=True)
    #
    # # 2. Alter the column with an explicit USING cast
    # op.execute("ALTER TABLE users ALTER COLUMN role TYPE role USING role::role")
    #
    # # 3. Set NOT NULL and default
    # op.alter_column(
    #     "users",
    #     "role",
    #     nullable=False,
    #     server_default=sa.text("'user'")
    # )



def downgrade() -> None:
    pass
    # # 1. Revert column type back to string
    # op.execute("ALTER TABLE users ALTER COLUMN role TYPE VARCHAR(255)")
    #
    # # 2. Drop the ENUM type
    # sa.Enum(Role, name="role").drop(op.get_bind(), checkfirst=True)
