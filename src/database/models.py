from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Record(BaseModelModify):
    time_start: str
    user_id: str
    staff_id: int
    service_id: int


class Service(BaseModelModify):
    name: str
    price: int
    duration: int


class Review(BaseModelModify):
    name: str
    age: int
    staff_id: int


class History(BaseModelModify):
    record_id: int


class User(BaseModelModify):
    name: str
    password: str


class Staff(User):
    post: str


class UserAuth(BaseModel):
    name: str
    password: str

