from turtle import title
from sqlalchemy.orm import Session
from agente import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    emprestimos = db.query(models.Emprestimo).all()
    return emprestimos


def create(request: schemas.Emprestimo, db: Session):
    #vrifica se a zona existe
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")
    #gravar os dados
    new_emprestimo = models.Emprestimo(name=request.name, computador_id_send=request.computador_id_send, id_zona=request.id_zona)
    #criar um novo
    db.add(new_emprestimo)
    db.commit()
    db.refresh(new_emprestimo)
    return new_emprestimo


def destroy(id: int, db: Session):
    #verifica se existe o dado
    emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == id)

    if not emprestimo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Emprestimo with id {id} not found")
    #apaga
    emprestimo.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int, request: schemas.Emprestimo, db: Session):
    #vrifica se a zona existe
    zona = db.query(models.Zona).filter(models.Zona.id == request.id_zona)

    if not zona.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Zona with id {request.id_zona} not found")
    #pega os dados
    emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == id)

    if not emprestimo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Emprestimo with id {id} not found")
    #altera os dados
    emprestimo.update(request.dict())
    db.commit()
    return 'updated'
    


def show(id: int, db: Session):
    #pega os dados
    emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == id).first()
    if not emprestimo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Emprestimo with the id {id} is not available")
    return emprestimo
