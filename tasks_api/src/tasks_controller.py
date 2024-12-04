from sqlmodel import Session, select

from src.database import get_engine
from .models import RequestTask, Task
from fastapi import APIRouter


router = APIRouter()


@router.post('/tasks')
def task_create(task: RequestTask):
  # https://github.com/fastapi/sqlmodel/discussions/1007
  valid_task = RequestTask.model_validate(task)
  task = Task(**valid_task.model_dump())
  
  session = Session(get_engine())
  session.add(task)
  session.commit()
  session.refresh(task)

  return task


@router.get('/tasks')
def task_list():
  session = Session(get_engine())
  sttm = select(Task)

  tasks = session.exec(sttm).all()

  return tasks