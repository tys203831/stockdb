"""empty message

Revision ID: 0a0d5dfcd2a7
Revises: 7de8d9d52cba
Create Date: 2023-08-16 20:54:08.127992

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
import logging
from app.decorators import log_start_end
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a0d5dfcd2a7'
down_revision = '7de8d9d52cba'
branch_labels = None
depends_on = None

logger = logging.getLogger(__name__)

@log_start_end(log=logger)
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dim_data_vendor', 'website_url',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('dim_data_vendor', 'support_email',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###

@log_start_end(log=logger)
def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dim_data_vendor', 'support_email',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('dim_data_vendor', 'website_url',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
