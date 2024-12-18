from datetime import date, datetime
import datetime
from sqlmodel import Relationship, SQLModel, Field

class BaseUser(SQLModel):
  name: str
  email: str
  username: str


class User(BaseUser, table=True):
  id: int = Field(default=None, primary_key=True)
  password: str

  tasks: list["Task"] = Relationship(back_populates="user")


class SignUpUserRequest(BaseUser):
  password: str
  confirm_password: str


class SignInUserRequest(SQLModel):
  username: str
  password: str


class BaseTask(SQLModel):
  title: str
  description: str
  done: bool
  # Mudar para Datetime
  created_at: str = Field(default=datetime.datetime.now().strftime('%Y-%m-%d'))
  due_date: date

  # relacionamentos
  user_id: int | None = Field(default=None, foreign_key="user.id")
  


class Task(BaseTask, table=True):
  id: int = Field(default=None, primary_key=True)
  user: User | None = Relationship(back_populates="tasks")


class TaskPublic(BaseTask):
  user: BaseUser | None


class CreateTaskRequest(BaseTask):
  pass



