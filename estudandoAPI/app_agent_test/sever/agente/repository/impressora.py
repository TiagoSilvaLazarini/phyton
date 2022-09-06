from sqlalchemy.orm import Session
from agente import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    impressoras = db.query(models.Impressora).all()
    return impressoras


def create(request: schemas.Impressora, db: Session):
    #vrifica se a zona existe
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")

    #gravar os dados
    new_impressora = models.Impressora(ip=request.ip, name=request.name, id_zona=request.id_zona)
    #criar um novo
    db.add(new_impressora)
    db.commit()
    db.refresh(new_impressora)
    return new_impressora


def destroy(id: int, db: Session):
    #verifica se existe o dado
    impressora = db.query(models.Impressora).filter(models.Impressora.id == id)

    if not impressora.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Impressora with id {id} not found")
    #apaga
    impressora.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int, request: schemas.Impressora, db: Session):
    #vrifica se a zona existe
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")
    #pega os dados
    impressora = db.query(models.Impressora).filter(models.Impressora.id == id)

    if not impressora.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Impressora with id {id} not found")
    #altera os dados
    impressora.update(request.dict())
    db.commit()
    return 'updated'
    


def show(id: int, db: Session):
    #pega os dados
    impressora = db.query(models.Impressora).filter(models.Impressora.id == id).first()
    if not impressora:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Impressora with the id {id} is not available")
    return impressora
