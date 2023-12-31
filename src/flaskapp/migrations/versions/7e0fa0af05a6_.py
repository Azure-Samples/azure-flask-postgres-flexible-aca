"""empty message

Revision ID: 7e0fa0af05a6
Revises:
Create Date: 2023-06-29 22:52:53.406543

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7e0fa0af05a6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cruise",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "destination",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "info_request",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("notes", sa.String(length=255), nullable=False),
        sa.Column("cruise_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "cruise_destination_link",
        sa.Column("destination_id", sa.Integer(), nullable=False),
        sa.Column("cruise_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["cruise_id"],
            ["cruise.id"],
        ),
        sa.ForeignKeyConstraint(
            ["destination_id"],
            ["destination.id"],
        ),
        sa.PrimaryKeyConstraint("destination_id", "cruise_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("cruise_destination_link")
    op.drop_table("info_request")
    op.drop_table("destination")
    op.drop_table("cruise")
    # ### end Alembic commands ###
