"""notifications

Revision ID: 939c7abd8911
Revises: 01bec3913c47
Create Date: 2025-01-31 22:46:37.378820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '939c7abd8911'
down_revision = '01bec3913c47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Float(), nullable=False),
    sa.Column('payload_json', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_notification_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_notification_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_notification_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_notification_user_id'))
        batch_op.drop_index(batch_op.f('ix_notification_timestamp'))
        batch_op.drop_index(batch_op.f('ix_notification_name'))

    op.drop_table('notification')
    # ### end Alembic commands ###
