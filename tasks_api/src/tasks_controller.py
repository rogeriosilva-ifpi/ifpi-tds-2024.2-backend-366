from sqlmodel import Session, select

from src.database import get_engine
from .models import Task
from fastapi import APIRouter


router = APIRouter()


@router.post('/tasks')
def task_create(task: Task):
  
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