from sqlalchemy.exc import IntegrityError

from . import db_connection
from sqlalchemy import select
from sqlalchemy import insert
from .tables import table_cache


def delete_key(key: str = None, key_id: str = None) -> bool:
    if key:
        stmt = table_cache.delete().where(key == table_cache.columns.key)
        db_connection.execute(stmt)
        return True
    elif key_id:
        stmt = table_cache.delete().where(key == table_cache.columns.key)
        db_connection.execute(stmt)
        return True


def is_key_exists(key: str) -> bool:
    stmt = select([
        table_cache.columns.value,
    ]).where(key == table_cache.columns.key).order_by(table_cache.columns.cached_date.desc())

    result = db_connection.execute(stmt).fetchall()
    return result


def get_cache(key: str) -> str or None:
    message = 'OK'
    stmt = select([table_cache.columns.value]).where(key == table_cache.columns.key)\
        .order_by(table_cache.columns.cached_date.desc())

    result = db_connection.execute(stmt).fetchall()
    if not result:
        message = f'key {key} not found'
        return None, message

    return result[0][0], message


def insert_new_key(key: str, value: str) -> bool:
    stmt = (insert(table_cache).values(key=key, value=value))
    try:
        db_connection.execute(stmt)
    except IntegrityError:
        return False

    return True


def set_cache(key: str, value: str) -> tuple:
    message = 'OK'
    if is_key_exists(key):
        delete_key(key=key)
        message = 'key was already exists and has been deleted. The new key is added'
    insert_new_key(key, value)

    return True, message
