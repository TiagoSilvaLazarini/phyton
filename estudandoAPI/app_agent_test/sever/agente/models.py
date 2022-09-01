from sqlalchemy import Column, Integer, String, ForeignKey
from agente.database import Base
from sqlalchemy.orm import relationship
import loger
from agente import schemas


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    


class Impressora(Base):
    __tablename__ = 'impressoras'

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    name = Column(String)
    id_zona = Column(Integer, ForeignKey("zonas.id"))

    #relacionamentos -filho
    zona_im = relationship('Zona', back_populates="impressoras_z")


class Computador(Base):
    __tablename__ = 'computadores'

    id = Column(Integer, primary_key=True, index=True)
    id_net = Column(String)
    ip = Column(String)
    name = Column(String)
    id_zona = Column(Integer, ForeignKey("zonas.id"))

    #relacionamentos -pai
    emprestimos = relationship('Emprestimo', back_populates="computador_emp")
    #relacionamentos -filho
    zona_pc = relationship('Zona', back_populates="computadores_z")


class Emprestimo(Base):
    __tablename__ = 'emprestimos'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    computador_id_send = Column(Integer, ForeignKey("computadores.id"))
    id_zona = Column(Integer, ForeignKey("zonas.id"))
    
    #relacionamentos -filho
    computador_emp = relationship('Computador', back_populates="emprestimos")
    zona_em = relationship('Zona', back_populates="emprestimos_z")


class Zona(Base):
    __tablename__ = 'zonas'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    #relacionamentos -pai
    computadores_z = relationship('Computador', back_populates="zona_pc")
    impressoras_z = relationship('Impressora', back_populates="zona_im")
    emprestimos_z = relationship('Emprestimo', back_populates="zona_em")

class CMD(Base):
    __tablename__ = 'cmds'

    id = Column(Integer, primary_key=True, index=True)
    comando = Column(String)
        
    