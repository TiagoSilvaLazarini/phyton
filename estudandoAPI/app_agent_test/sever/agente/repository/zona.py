from sqlalchemy.orm import Session
from agente import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    Zonas = db.query(models.Zona).all()
    return Zonas


def create(request: schemas.Zona, db: Session):
    #gravar os dados
    new_zona = models.Zona(name=request.name)
    #criar um novo
    db.add(new_zona)
    db.commit()
    db.refresh(new_zona)
    return new_zona


def destroy(id: int, db: Session):
    #verifica se existe o dado
    zona = db.query(models.Zona).filter(models.Zona.id == id)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {id} not found")
    #apaga
    zona.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


def update(id: int, request: schemas.Zona, db: Session):
    #pega os dados
    zona = db.query(models.Zona).filter(models.Zona.id == id)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {id} not found")
    #altera os dados
    zona.update(request.dict())
    db.commit()
    return 'updated'
    


def show(id: int, db: Session):
    #pega os dados
    zona = db.query(models.Zona).filter(models.Zona.id == id).first()
    if not zona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with the id {id} is not available")
    return zona
