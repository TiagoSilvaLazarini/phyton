from turtle import title
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from agente import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from agente.repository import cmd

router = APIRouter(
    #prefixo antes da rota
    prefix="/cmd",
    #grupo que esta
    tags=['Comandos']
)

get_db = database.get_db

#get all
@router.get('/', response_model=List[schemas.ShowCMD])
def all(db: Session = Depends(get_db)):
    return cmd.get_all(db)

#send new
@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.CMD, db: Session = Depends(get_db)):
    return cmd.create(request, db)

#delete 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return cmd.destroy(id, db)

#update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.CMD, db: Session = Depends(get_db)):
    return cmd.update(id, request, db)

#get from id
@router.get('/{id}', status_code=200, response_model=schemas.ShowCMD)
def show(id: int, db: Session = Depends(get_db)):
    return cmd.show(id, db)
