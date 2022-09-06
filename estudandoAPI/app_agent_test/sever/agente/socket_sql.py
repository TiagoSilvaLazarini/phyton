from argparse import Action
from agente import schemas, database, models, oauth2
from datetime import datetime
from agente import encrypt
import loger

def get_cmd(id):
    with database.SessionLocal() as session:
        result = session.query(models.CMD.comando).order_by(models.CMD.id.asc()).where(models.CMD.id == id)
    return result

def get_cmd_config():
    with database.SessionLocal() as session:
        result = session.query(models.CMD_order.name,models.CMD_order.comando).order_by(models.CMD_order.id.asc()).where(models.CMD_order.type == "config")

    lista = []
    for row in result:
        lista.append({"id":row[0],"cmd":row[1]})
    return lista

def get_cmd_request():
    with database.SessionLocal() as session:
        result = session.query(models.CMD_order.name,models.CMD_order.comando).order_by(models.CMD_order.id.asc()).where(models.CMD_order.type == "request")

    lista = []
    for row in result:
        lista.append({"name":row[0],"cmd":row[1]})
    return lista

def set_pc(pc):

    net_adress=pc.get("net_adress")
    name_pc = pc.get("name_pc")
    ip_pc=pc.get("ip_pc")
    with database.SessionLocal() as session:
        result = session.query(models.Computador).filter(models.Computador.id_net == net_adress)

        if(result == True):
            new_computador = models.Computador(id_net=net_adress,ip=ip_pc,name=name_pc,id_zona=1)
            session.add(new_computador)
            session.commit()
            session.refresh(new_computador)
            loger.logger.debug("computador cadastrado")
        else:
            loger.logger.debug("esse computador já está cadastrado")
            pass


def save_data(request):
    set_pc(request.get("pc"))