"""4th migrate

Revision ID: f55546c2fe48
Revises: 07a82e4d51aa
Create Date: 2023-10-20 09:14:59.883539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f55546c2fe48'
down_revision = '07a82e4d51aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judul', sa.String(length=50), nullable=False),
    sa.Column('post', sa.Text(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('judul')
    )
    op.drop_index('judul', table_name='blogs')
    op.drop_table('blogs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('judul', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('post', mysql.TEXT(), nullable=False),
    sa.Column('datetime', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('judul', 'blogs', ['judul'], unique=False)
    op.drop_table('Blogs')
    # ### end Alembic commands ###
