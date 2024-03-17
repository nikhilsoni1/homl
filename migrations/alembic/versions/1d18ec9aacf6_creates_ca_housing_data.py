"""creates ca_housing_data

Revision ID: 1d18ec9aacf6
Revises: 
Create Date: 2024-03-17 11:42:53.300671

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d18ec9aacf6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ca_housing_data",
        sa.Column("row_id", sa.Integer, primary_key=True),
        sa.Column("longitude", sa.Float),
        sa.Column("latitude", sa.Float),
        sa.Column("housing_median_age", sa.Float),
        sa.Column("total_rooms", sa.Float),
        sa.Column("total_bedrooms", sa.Float),
        sa.Column("population", sa.Float),
        sa.Column("households", sa.Float),
        sa.Column("median_income", sa.Float),
        sa.Column("median_house_value", sa.Float),
        sa.Column("ocean_proximity", sa.String),
    )


def downgrade() -> None:
    op.drop_table("ca_housing_data")
