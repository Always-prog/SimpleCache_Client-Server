"""HERE IS OUR TABLES :P"""
from . import engine

from sqlalchemy import Table, Column, MetaData, Integer, String, Identity, inspect, DateTime, func
from typing import List, Optional

# Tables #
table_cache = Table('CACHE_KEY_VALUE', MetaData(),
                    Column('id', Integer, Identity(start=42, cycle=True), primary_key=True),
                    Column('key', String, unique=True),
                    Column('value', String),
                    Column('cached_date', DateTime(timezone=True), server_default=func.now())
                    )

TABLES = [var for varname, var in locals().items() if 'table_' in varname]


def create_not_exists_tables(tables: Optional[List[Table]] = TABLES) -> None:
    inspector = inspect(engine)
    for table in tables:
        if not inspector.has_table(table.name):
            table.create(engine)  # sqlalchemy by himself logging creating tables


# Create tables if it not exists
create_not_exists_tables()
