from argparse import Action
from agente import schemas, database, models, oauth2
from datetime import datetime
from agente import encrypt,socket_sql
import loger


def set_computador(pc):
    pass 

def get_curent_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_json_return(request):
    action = request.get("action")
    pc = set_computador(request.get("pc"))
    content = {"action":action,"result": get_curent_time(),"encrypt_key":encrypt.generate_key(),"request":socket_sql.get_cmd_request(),"comando":socket_sql.get_cmd_config()}
    loger.logger.debug("creating msg to cliente action: test")
    
    return content
