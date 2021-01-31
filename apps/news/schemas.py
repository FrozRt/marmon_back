from typing import Optional, Union

from pydantic import BaseModel


class NewsSchemaIn(BaseModel):
    slug: str
    author_id: Union[int, str]
    topic_id: Optional[Union[int, str]]
    title: str
    text: str
    html: Optional[str]
    image_id: Optional[Union[int, str]]
    is_visible = Optional[bool]
    is_commentable = Optional[bool]
    is_public = Optional[bool]


class NewsSchemaOut(NewsSchemaIn):
    id: Union[str, int]