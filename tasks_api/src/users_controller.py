from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from src.auth_utils import get_logged_user
from src.database import get_engine
from src.models import BaseUser, SignInUserRequest, SignUpUserRequest, User
from passlib.context import CryptContext
import jwt

router = APIRouter()

SECRET_KEY = '02a7e6efa2d0f77fc89f1f44d73acd7bf26e5dc6f3c1f939ff5d038ea3604f23'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 10
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 3 # Vale 3 dias

@router.post('/signup', response_model=BaseUser)
def signup(user_data: SignUpUserRequest):
  if user_data.password != user_data.confirm_password:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail='Senhas não coincidem!')
  # Hash da senha
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  hash = pwd_context.hash(user_data.password)
  
  user = User(email=user_data.email, 
    name=user_data.name, 
    username=user_data.username,
    password=hash)
  
  with Session(get_engine()) as session:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
  

@router.post('/signin')
def signin(signin_data: SignInUserRequest):
  with Session(get_engine()) as session:
    # pegar usuário por username
    
    sttm = select(User).where(User.username == signin_data.username)
    user = session.exec(sttm).first()
    print('1: ', user)
    if not user: # não encontrou usuário
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
        detail='Usuário e/ou senha incorreto(S)')
    
    # encontrou, então verificar a senha
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    print('2: ', user)
    is_correct = pwd_context.verify(signin_data.password, user.password)

    if not is_correct:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail='Usuário e/ou senha incorrento(S)')
    
    # Tá tudo OK pode gerar um Token JWT e devolver
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({'sub': user.username, 'exp': expires_at}, key=SECRET_KEY, algorithm=ALGORITHM)

    expires_rt = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = jwt.encode({'sub': user.username, 'exp': expires_rt}, key=SECRET_KEY, algorithm=ALGORITHM)


    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/me', response_model=BaseUser)
def me(user: Annotated[User, Depends(get_logged_user)]):
  return user
