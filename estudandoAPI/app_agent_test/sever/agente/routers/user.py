from agente import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from agente.repository import user

router = APIRouter(
    #prefixo antes da rota
    prefix="/user",
    #grupo que esta
    tags=['Users']
)

get_db = database.get_db

#send new
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


#get from id
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
