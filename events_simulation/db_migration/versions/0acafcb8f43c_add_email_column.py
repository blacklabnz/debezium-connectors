"""add email column

Revision ID: 0acafcb8f43c
Revises: 
Create Date: 2025-10-22 11:12:21.048325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0acafcb8f43c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('events', sa.Column('email', sa.String(450), unique=False, nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('events', 'email')
    pass
