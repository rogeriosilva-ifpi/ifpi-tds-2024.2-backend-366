from sqlmodel import create_engine

def get_engine():
  return create_engine('sqlite:///clubes.db')