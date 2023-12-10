from pydantic import BaseModel


class class_todo(BaseModel):
    id: int
    item: str