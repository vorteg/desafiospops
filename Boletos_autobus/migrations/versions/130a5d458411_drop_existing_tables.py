"""Drop existing tables

Revision ID: 130a5d458411
Revises: b0f37b37c92f
Create Date: 2024-06-12 12:29:04.479687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '130a5d458411'
down_revision: Union[str, None] = 'b6ffda0dfa12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Eliminar las tablas en orden inverso de creación para evitar problemas de FK
    op.drop_table('boletos')
    op.drop_table('asientos')
    op.drop_table('usuarios')


def downgrade() -> None:
    pass
