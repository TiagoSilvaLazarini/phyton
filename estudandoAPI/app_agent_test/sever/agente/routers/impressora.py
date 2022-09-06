from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from agente import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from agente.repository import impressora

router = APIRouter(
    #prefixo antes da rota
    prefix="/impressora",
    #grupo que esta
    tags=['Impressoras']
)

get_db = database.get_db

#get all
@router.get('/', response_model=List[schemas.ShowImpressora])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return impressora.get_all(db)

#send new
@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Impressora, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return impressora.create(request, db)

#delete 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return impressora.destroy(id, db)

#update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Impressora, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return impressora.update(id, request, db)

#get from id
@router.get('/{id}', status_code=200, response_model=schemas.ShowImpressora)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return impressora.show(id, db)
