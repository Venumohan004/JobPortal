"""add application status history

Revision ID: 846d7bf601fc
Revises: 276ea069842a
Create Date: 2026-07-24 17:33:58.668932

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "846d7bf601fc"
down_revision = "276ea069842a"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "application_status_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("application_id", sa.Integer(), nullable=False),
        sa.Column("old_status", sa.String(length=50), nullable=False),
        sa.Column("new_status", sa.String(length=50), nullable=False),
        sa.Column("changed_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["application_id"],
            ["applications.id"]
        ),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade():
    op.drop_table("application_status_history")