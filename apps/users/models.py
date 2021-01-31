from typing import Any

from sqlalchemy import Table, Column, Integer, String, Text, DateTime, Boolean, func, ForeignKey

from database import metadata


User: Any = Table(
    'post', metadata,
    Column('id', Integer, primary_key=True),