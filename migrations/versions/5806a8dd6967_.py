"""empty message

Revision ID: 5806a8dd6967
Revises: 
Create Date: 2019-02-27 21:48:07.179338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5806a8dd6967'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.Column('nickname', sa.String(length=32), nullable=True, comment='用户名'),
    sa.Column('email', sa.String(length=50), nullable=False, comment='邮箱'),
    sa.Column('password', sa.String(length=32), nullable=False, comment='密码'),
    sa.Column('secret_token', sa.String(length=32), nullable=False, comment='访问密匙'),
    sa.Column('salt', sa.String(length=32), nullable=False, comment='密码盐'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='上传的用户'),
    sa.Column('default_show', sa.String(length=200), nullable=True, comment='默认上传显示的地址'),
    sa.Column('raw', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.drop_table('user')
    # ### end Alembic commands ###
