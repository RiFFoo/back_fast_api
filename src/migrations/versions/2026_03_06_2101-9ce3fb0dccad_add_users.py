"""add users

Revision ID: 9ce3fb0dccad
Revises: ef9c37460952
Create Date: 2026-03-06 21:01:38.616643

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9ce3fb0dccad"
down_revision: Union[str, None] = "ef9c37460952"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")