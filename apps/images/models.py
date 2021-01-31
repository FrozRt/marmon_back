from typing import Any

from sqlalchemy import Table, Column, Integer, String
from database import metadata


Image: Any = Table(
    'image', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(250), nullable=False),
    Column('url', String(250), nullable=False),
    Column('width', Integer, nullable=True),
    Column('height', Integer, nullable=True),
)
