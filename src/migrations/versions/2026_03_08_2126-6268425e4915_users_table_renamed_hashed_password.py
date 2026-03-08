"""users table renamed hashed_password

Revision ID: 6268425e4915
Revises: 9ce3fb0dccad
Create Date: 2026-03-08 21:26:14.129935

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6268425e4915"
down_revision: Union[str, None] = "9ce3fb0dccad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users", sa.Column("hashed_password", sa.String(length=200), nullable=False)
    )
    op.drop_column("users", "password")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "password", sa.VARCHAR(length=200), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("users", "hashed_password")