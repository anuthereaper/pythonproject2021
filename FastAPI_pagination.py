# https://github.com/uriyyo/fastapi-pagination/blob/main/docs/index.md 
from fastapi import FastAPI
from pydantic import BaseModel

from typing import TypeVar, Generic
from fastapi import Query
from fastapi_pagination import Page, add_pagination, paginate, Params
from fastapi_pagination import LimitOffsetPage  # for Limit n Offset
from fastapi_pagination.default import Page as BasePage, Params as BaseParams

T = TypeVar("T")
class Params(BaseParams):
    size: int = Query(3, ge=1, le=1_000, description="Page size")   # custom page size

class Page(BasePage[T], Generic[T]):
    __params_type__ = Params

app = FastAPI()

# structure of data
class User(BaseModel):
    name: str
    surname: str

# Data to be paged through
users = [
    User(name='Yurii', surname='Karabas'),User(name='B1', surname='B1'),User(name='C1', surname='C1'),User(name='D1', surname='D1'),User(name='E1', surname='E1'),
    User(name='Yurii', surname='Karabas'),User(name='B1', surname='B1'),User(name='C1', surname='C1'),User(name='D1', surname='D1'),User(name='E1', surname='E1'),
    User(name='Yurii', surname='Karabas'),User(name='B1', surname='B1'),User(name='C1', surname='C1'),User(name='D1', surname='D1'),User(name='E1', surname='E1')
    # ...
]

@app.get('/users', response_model=Page[User])                 # respond with page and size
#@app.get('/users', response_model=LimitOffsetPage[User])     # respond with limit n offset 
async def get_users():
    return paginate(users)

add_pagination(app)