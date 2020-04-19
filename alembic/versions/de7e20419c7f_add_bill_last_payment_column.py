"""Add bill.last_payment column

Revision ID: de7e20419c7f
Revises: 
Create Date: 2020-04-19 14:54:35.447835
"""
from typing import Optional
from alembic import op
from sqlalchemy import DateTime, Column

revision: str = "de7e20419c7f"
down_revision: Optional[str] = None
branch_labels: Optional[str] = None
depends_on: Optional[str] = None


def upgrade() -> None:
    """Upgrades migration."""
    op.add_column("bills", Column("last_payment", DateTime(), nullable=True))
    op.create_index(op.f("ix_bills_last_payment"), "bills", ["last_payment"], unique=False)


def downgrade() -> None:
    """Downgrades migration."""
    op.drop_index(op.f("ix_bills_last_payment"), table_name="bills")
    op.drop_column("bills", "last_payment")
