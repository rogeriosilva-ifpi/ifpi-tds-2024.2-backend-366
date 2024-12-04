from sqlmodel import Session, select

from src.database import get_engine
from .models import CreateTaskRequest, Task
from fastapi import APIRouter, HTTPException, status, Response


router = APIRouter()


@router.post('/tasks')
def task_create(task: CreateTaskRequest):

  valid_task = Task.model_validate(task)
  
  session = Session(get_engine())
  session.add(valid_task)
  session.commit()
  session.refresh(valid_task)

  return valid_task


@router.delete('/tasks/{task_id}')
def task_delete(task_id: int):
  session = Session(get_engine())

  sttm = select(Task).where(Task.id == task_id)
  task = session.exec(sttm).first()

  if not task:
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='Task nao encontrada...')
  
  else:
    session.delete(task)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
  

@router.get('/tasks')
def task_list():
  session = Session(get_engine())
  sttm = select(Task)

  tasks = session.exec(sttm).all()

  return tasks


@router.post('/tasks/{task_id}/done')
def task_mask_as_done(task_id: int):
  with Session(get_engine()) as session:
    sttm = select(Task).where(Task.id == task_id)
    task = session.exec(sttm).first()
    if not task: 
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='Task nao encontrada...')
    
    task.done = True
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  