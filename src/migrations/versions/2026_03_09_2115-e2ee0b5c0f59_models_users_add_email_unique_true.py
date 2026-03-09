"""models/users add email unique=True

Revision ID: e2ee0b5c0f59
Revises: 6268425e4915
Create Date: 2026-03-09 21:15:28.782069

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e2ee0b5c0f59"
down_revision: Union[str, None] = "6268425e4915"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(None, "users", ["email"])

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, "users", type_="unique")