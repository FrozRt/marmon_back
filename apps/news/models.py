from typing import Any

from sqlalchemy import Table, Column, Integer, String, Text, DateTime, Boolean, func, ForeignKey

from database import metadata


Post: Any = Table(
    'post', metadata,
    Column('id', Integer, primary_key=True),
    Column('slug', String(64), unique=True, index=True, nullable=False),

    Column('author_id',  Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=True),
    Column('topic_id', Integer, ForeignKey('user.id', ondelete='SET NULL'), nullable=True),

    Column('title', String(64), nullable=False),
    Column('text', Text, nullable=False, server_default='text'),
    Column('html', Text, nullable=True),
    Column('image_id', Integer, ForeignKey('image.id', ondelete='SET NULL'), nullable=True),

    Column('created_at', DateTime, default=func.now(), nullable=True),
    Column('updated_at', DateTime, onupdate=func.now(), server_default=func.now(), nullable=True),
    Column('deleted_at', DateTime, index=True, nullable=True),

    Column('is_visible', Boolean, default=True),
    Column('is_commentable', Boolean, default=True),
    Column('is_public', Boolean, default=True),  # special or the poor man's post
)
