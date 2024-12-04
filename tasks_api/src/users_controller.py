from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from src.database import get_engine
from src.models import BaseUser, SignInUserRequest, SignUpUserRequest, User
from passlib.context import CryptContext

router = APIRouter()

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
        detail='Usuário e/ou senha incorrento(S)')
    
    # encontrou, então verificar a senha
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    print('2: ', user)
    is_correct = pwd_context.verify(signin_data.password, user.password)

    if not is_correct:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail='Usuário e/ou senha incorrento(S)')

    return {'Token': 'Esse é seu crachá'}


