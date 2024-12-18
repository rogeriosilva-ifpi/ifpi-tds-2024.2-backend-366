from encodings.punycode import selective_len
from typing import Annotated
from sqlmodel import Session, select

from src.auth_utils import get_logged_user
from src.database import get_engine
from .models import CreateTaskRequest, Task, TaskPublic, User
from fastapi import APIRouter, Depends, HTTPException, status, Response


router = APIRouter()


@router.post('/tasks')
def task_create(task: CreateTaskRequest, user: Annotated[User, Depends(get_logged_user)]):

  valid_task = Task.model_validate(task)
  valid_task.user_id = user.id
  
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
  

@router.get('/tasks', response_model=list[TaskPublic])
def task_list(user: Annotated[User, Depends(get_logged_user)]):
  session = Session(get_engine())
  sttm = select(Task).where(Task.user_id == user.id)

  tasks = session.exec(sttm).all()

  return tasks


@router.post('/tasks/{task_id}/done')
def task_mask_as_done(task_id: int, user: Annotated[User, Depends(get_logged_user)]):
  with Session(get_engine()) as session:
    sttm = select(Task).where(Task.id == task_id).where(Task.user_id == user.id)
    task = session.exec(sttm).first()
    if not task: 
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='Task não encontrada!')
    
    # já encontrou
    if task.done:
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='Você já concluiu essa Tarefa!')

    
    task.done = True
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  