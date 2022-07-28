from turtle import title
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from agente import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from agente.repository import zona

router = APIRouter(
    #prefixo antes da rota
    prefix="/zona",
    #grupo que esta
    tags=['Zonas']
)

get_db = database.get_db

#get all
@router.get('/', response_model=List[schemas.ShowZonaAll])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zona.get_all(db)

#send new
@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Zona, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zona.create(request, db)

#delete 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zona.destroy(id, db)

#update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Zona, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zona.update(id, request, db)

#get from id
@router.get('/{id}', status_code=200, response_model=schemas.ShowZonaAll)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zona.show(id, db)
