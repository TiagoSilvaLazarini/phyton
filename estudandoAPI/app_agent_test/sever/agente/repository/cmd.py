from turtle import title
from unicodedata import name
from sqlalchemy.orm import Session
from agente import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    CMDS = db.query(models.CMD).all()
    return CMDS


def create(request: schemas.CMD, db: Session):
    #gravar os dados
    new_cmd = models.CMD(comando=request.comando)
    #criar um novo
    db.add(new_cmd)
    db.commit()
    db.refresh(new_cmd)
    return new_cmd


def destroy(id: int, db: Session):
    #verifica se existe o dado
    cmd = db.query(models.CMD).filter(models.CMD.id == id)

    if not cmd.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"CMD with id {id} not found")
    #apaga
    cmd.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


def update(id: int, request: schemas.CMD, db: Session):
    #pega os dados
    cmd = db.query(models.CMD).filter(models.CMD.id == id)

    if not cmd.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"CMD with id {id} not found")
    #altera os dados
    cmd.update(request.dict())
    db.commit()
    return 'updated'
    


def show(id: int, db: Session):
    #pega os dados
    cmd = db.query(models.CMD).filter(models.CMD.id == id).first()
    if not cmd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"CMD with the id {id} is not available")
    return cmd
