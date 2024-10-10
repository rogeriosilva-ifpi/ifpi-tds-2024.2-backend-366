from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Clube(BaseModel):
  id: int | None = None
  nome: str


clubes_futebol: list[Clube] = []

clube1 = Clube(id=1, nome='Vasco')
clubes_futebol.append(clube1)
clubes_futebol.append(Clube(id=2, nome='Flamengo'))


@app.get('/clubes', status_code=status.HTTP_200_OK)
def lista_clubes():
  return clubes_futebol


@app.get('/clubes/{clube_id}')
def detalhes_clube(clube_id: int):
  for clube in clubes_futebol:
    if clube.id == clube_id:
      return clube
  
  # nao localizou
  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'Clube não localizado com id = {clube_id}'
    )



@app.post('/clubes', status_code=status.HTTP_201_CREATED)
def criar_clube(novo_clube: Clube):
  clubes_futebol.append(novo_clube)
  return novo_clube