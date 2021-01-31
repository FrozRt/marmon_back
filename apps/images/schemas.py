from typing import Optional, Union

from pydantic import BaseModel


class ImageSchema(BaseModel):
    id: int
    name: Optional[str]
    url: str
    width: Optional[Union[int, str]]
    height: Optional[Union[int, str]]