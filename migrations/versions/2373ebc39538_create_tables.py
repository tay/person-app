"""Create tables

Revision ID: 2373ebc39538
Revises: 
Create Date: 2020-08-05 00:46:54.401744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2373ebc39538'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('middle_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sqlite_autoincrement=True
    )
    op.create_table('person_archive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('middle_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person_archive')
    op.drop_table('person')
    # ### end Alembic commands ###
