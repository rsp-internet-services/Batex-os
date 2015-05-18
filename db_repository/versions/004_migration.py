from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

order = Table('order', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('costumer', String(length=128)),
    Column('user_id', Integer),
    Column('order_items', Integer),
)

order_items = Table('order_items', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_order', Integer),
    Column('id_product', Integer),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=128)),
    Column('price', Float),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('password', String(length=64)),
    Column('user_name', String(length=128)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['order'].create()
    post_meta.tables['order_items'].create()
    post_meta.tables['product'].create()
    post_meta.tables['user'].columns['user_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['order'].drop()
    post_meta.tables['order_items'].drop()
    post_meta.tables['product'].drop()
    post_meta.tables['user'].columns['user_name'].drop()
