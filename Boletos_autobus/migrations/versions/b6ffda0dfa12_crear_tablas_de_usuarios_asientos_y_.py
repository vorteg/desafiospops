"""Crear tablas de usuarios, asientos y boletos

Revision ID: b6ffda0dfa12
Revises: 
Create Date: 2024-06-11 16:16:24.818512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6ffda0dfa12'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asientos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('fila', sa.String(length=1), nullable=True),
    sa.Column('disponible', sa.Boolean(), nullable=True),
    sa.Column('ubicacion', sa.Enum('VENTANA', 'PASILLO', name='ubicacion'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('tipo', sa.Enum('ADULTO', 'NINO', 'ADULTO_MAYOR', name='tipousuario'), nullable=True),
    sa.Column('profesion', sa.Enum('ESTUDIANTE', 'MAESTRO', 'NINGUNO', name='profesionusuario'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('boletos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asiento_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.Enum('ADULTO', 'NINO', 'ADULTO_MAYOR', name='tipousuario'), nullable=True),
    sa.ForeignKeyConstraint(['asiento_id'], ['asientos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boletos')
    op.drop_table('usuarios')
    op.drop_table('asientos')
    # ### end Alembic commands ###
