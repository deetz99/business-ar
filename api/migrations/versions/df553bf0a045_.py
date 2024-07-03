"""empty message

Revision ID: df553bf0a045
Revises: 0a47d4f8452d
Create Date: 2024-07-05 05:42:03.119293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df553bf0a045'
down_revision = '0a47d4f8452d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state', sa.String(length=5), nullable=True))
        batch_op.add_column(sa.Column('op_state', sa.String(length=5), nullable=True))
        batch_op.add_column(sa.Column('corp_class', sa.String(length=10), nullable=True))
        batch_op.create_index(batch_op.f('ix_business_corp_class'), ['corp_class'], unique=False)
        batch_op.create_index(batch_op.f('ix_business_op_state'), ['op_state'], unique=False)
        batch_op.create_index(batch_op.f('ix_business_state'), ['state'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_business_state'))
        batch_op.drop_index(batch_op.f('ix_business_op_state'))
        batch_op.drop_index(batch_op.f('ix_business_corp_class'))
        batch_op.drop_column('corp_class')
        batch_op.drop_column('op_state')
        batch_op.drop_column('state')

    # ### end Alembic commands ###