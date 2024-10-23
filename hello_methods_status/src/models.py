
# Refatoração: Melhorar a qualidade interna de um código
# sem alterar o seu comportamento observável

# PEP-8: Manual de Estilo de Código de Python

from sqlmodel import SQLModel, Field


class ClubeBase(SQLModel):
  nome: str = Field(min_length=3)
  serie: str = Field(min_length=1, max_length=1)


class Clube(ClubeBase, table=True):
  id: int | None = Field(default=None, primary_key=True)


class RequestClube(ClubeBase):
  pass