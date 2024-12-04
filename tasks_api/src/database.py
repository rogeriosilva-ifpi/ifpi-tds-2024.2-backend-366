from sqlmodel import create_engine, SQLModel


def get_engine():
  return create_engine('sqlite:///tarefas.db')


def init_db():
  SQLModel.metadata.create_all(get_engine())