from datetime import date, datetime
import datetime
from sqlmodel import SQLModel, Field


class BaseTask(SQLModel):
  title: str
  description: str
  done: bool
  created_at: str = Field(default=datetime.datetime.now().strftime('%Y-%m-%d'))
  due_date: date


class Task(BaseTask, table=True):
  id: int = Field(default=None, primary_key=True)


class CreateTaskRequest(BaseTask):
  pass



class BaseUser(SQLModel):
  name: str
  email: str
  username: str
  

class User(BaseUser, table=True):
  id: int = Field(default=None, primary_key=True)
  password: str


class SignUpUserRequest(BaseUser):
  password: str
  confirm_password: str


class SignInUserRequest(SQLModel):
  username: str
  password: str


