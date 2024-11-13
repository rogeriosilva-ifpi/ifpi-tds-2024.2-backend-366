from django import conf
from sqlmodel import create_engine
from decouple import config

def get_engine():
  # Usuário e Senha
  user = config('DB_USERNAME')
  password = config('DB_PASSWORD')
  # Nome do Banco de Dados
  db_name = config('DB_NAME')
  # Host e Porta
  host = config('DB_HOST')
  port = config('DB_PORT')
  # Montar a URL para conexão
  return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
  # return create_engine('sqlite:///banco_livros.db')