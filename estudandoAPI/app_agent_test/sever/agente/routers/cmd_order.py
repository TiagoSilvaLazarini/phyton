from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from agente import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from agente.repository import cmd_order

router = APIRouter(
    #prefixo antes da rota
    prefix="/cmd_order",
    #grupo que esta
    tags=['Comandos_order']
)

get_db = database.get_db

#get all
@router.get('/', response_model=List[schemas.ShowCMD_order])
def all(db: Session = Depends(get_db)):
    return cmd_order.get_all(db)

#send new
@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.CMD_order, db: Session = Depends(get_db)):
    return cmd_order.create(request, db)

#delete 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return cmd_order.destroy(id, db)

#update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.CMD_order, db: Session = Depends(get_db)):
    return cmd_order.update(id, request, db)

#get from id
@router.get('/{id}', status_code=200, response_model=schemas.ShowCMD_order)
def show(id: int, db: Session = Depends(get_db)):
    return cmd_order.show(id, db)