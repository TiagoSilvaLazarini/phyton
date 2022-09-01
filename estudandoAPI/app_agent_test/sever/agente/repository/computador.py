from turtle import title
from sqlalchemy.orm import Session
from agente import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    computadores = db.query(models.Computador).all()
    return computadores


def create(request: schemas.Computador, db: Session):
    #verifica se existe a zona
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")
    #gravar os dados
    new_computador = models.Computador(id_net=request.id_net, ip=request.ip, name=request.name, id_zona=request.id_zona)
    #criar um novo
    db.add(new_computador)
    db.commit()
    db.refresh(new_computador)
    return new_computador


def destroy(id: int, db: Session):
    #verifica se existe o dado
    computador = db.query(models.Computador).filter(models.Computador.id == id)

    if not computador.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Computador with id {id} not found")
    #apaga
    computador.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int, request: schemas.Computador, db: Session):
    #vrifica se a zona existe
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")
    #pega os dados
    computador = db.query(models.Computador).filter(models.Computador.id == id)

    if not computador.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Computador with id {id} not found")
    #altera os dados
    computador.update(request.dict())
    db.commit()
    return 'updated'
    


def show(id: int, db: Session):
    #pega os dados
    computador = db.query(models.Computador).filter(models.Computador.id == id).first()
    if not computador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Computador with the id {id} is not available")
    return computador
