from typing import List, Optional
from pydantic import BaseModel

#base do JSON
class ComputadorBase(BaseModel):
    id_net:str
    ip:str
    name:str
    id_zona: int

class Computador(ComputadorBase):
    class Config():
        orm_mode = True

class ImpressoraBase(BaseModel):
    ip:str
    name: str
    id_zona: int

class Impressora(ImpressoraBase):
    class Config():
        orm_mode = True

class EmprestimoBase(BaseModel):
    name: str
    computador_id_send:int
    id_zona: int

class Emprestimo(EmprestimoBase):
    class Config():
        orm_mode = True

class ZonaBase(BaseModel):
    name: str

class Zona(ZonaBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True


class ShowZona(BaseModel):
    id:int
    name: str
    class Config():
        orm_mode = True


class ShowComputador(BaseModel):
    id:int
    id_net:str
    ip:str
    name:str
    zona_pc: ShowZona
    class Config():
        orm_mode = True

class ShowImpressora(BaseModel):
    id:int
    ip:str
    name: str
    zona_im: ShowZona
    class Config():
        orm_mode = True


class ShowEmprestimo(BaseModel):
    id:int
    name: str
    computador_id_send:int
    zona_em: ShowZona

    class Config():
        orm_mode = True



class ShowZonaAll(ShowZona):
    computadores_z : List[Computador] =[]
    impressoras_z : List[Impressora] =[]
    emprestimos_z : List[Emprestimo] =[]


    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
