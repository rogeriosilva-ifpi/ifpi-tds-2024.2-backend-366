from datetime import datetime
from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  title: str
  description: str
  done: bool
  due_date: datetime



class User(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str
  email: str
  username: str
  password: str