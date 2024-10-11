from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    id: str
    name: str
    author: str
    isbn: str
    rating: float
    publish_date: datetime

class Success(BaseModel):
    message: str
    id: str

class Error(BaseModel):
    message: str
