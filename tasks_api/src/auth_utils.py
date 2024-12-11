from datetime import datetime, timedelta, timezone
from typing import Annotated, Literal
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlmodel import Session, select

from src.database import get_engine
from src.models import User

# Retaforar depois(antes do Natal)
SECRET_KEY = '02a7e6efa2d0f77fc89f1f44d73acd7bf26e5dc6f3c1f939ff5d038ea3604f23'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='signin')

async def get_logged_user(token: Annotated[str, Depends(oauth2_scheme)]):
  # Vai pegar o Token na Request, se válido
  # pegará o usuário no BD para confirmar e retornar ele
  exception = HTTPException(status_code=401, detail='Não autorizado!')

  try:
    username = decode_token(token)
  except:
    raise exception
  
  if not username: 
    raise exception
  
  # Pegar usuário completo no BD
  with Session(get_engine()) as session:
    sttm = select(User).where(User.username == username)
    user = session.exec(sttm).first()

    if not user:
      raise exception
    
    return user


# HASH Password
def hash_password(plain_password: str):
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  hash = pwd_context.hash(plain_password)
  return hash


def verify_hash(plain_password: str, hashed_password: str):
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  is_correct = pwd_context.verify(plain_password, hashed_password)
  return is_correct


# JWT Token
SECRET_KEY = '02a7e6efa2d0f77fc89f1f44d73acd7bf26e5dc6f3c1f939ff5d038ea3604f23'
ALGORITHM = 'HS256'
ACCESS_EXPIRES = 10 # 10 minutos
REFRESH_EXPIRES = 60 * 24 * 3 # Vale 3 dias

def generate_token(sub: str, token_type: Literal['access', 'refresh']):
  expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_EXPIRES)
  
  if token_type == 'refresh':
    expires = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_EXPIRES)
  
  token = jwt.encode({'sub': sub, 'exp': expires}, key=SECRET_KEY, algorithm=ALGORITHM)
  return token


def decode_token(token: str):
  payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
  return payload.get('sub')


