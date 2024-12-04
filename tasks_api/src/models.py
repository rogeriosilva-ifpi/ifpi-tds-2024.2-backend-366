from datetime import date
from sqlmodel import SQLModel, Field


class BaseTask(SQLModel):
  title: str
  description: str
  done: bool
  due_date: date


class Task(BaseTask, table=True):
  id: int = Field(default=None, primary_key=True)


class RequestTask(BaseTask):
  pass  


class User(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str
  email: str
  username: str
  password: str