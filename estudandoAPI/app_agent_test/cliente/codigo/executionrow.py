import subprocess
import json
from codigo import app_client
import loger

_estado = False

def estado_con(estado:bool):
    global _estado
    _estado = estado

def get_estado_con():
    return _estado

# Comandos powershell
def commandspowershell(item):
    target= "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    return subprocess.getoutput([target, item])


# Data e hora do inicio da ultima linha de execução
def dateandhour():
    return commandspowershell("(get-date).ToString()")

def save_data(data):
    with open("./cliente/codigo/data_file.json", "w") as write_file:
        json.dump(data, write_file)


def get_data(type):
    loger.logger.debug("pegar os dados") 
    with open("./cliente/codigo/data_file.json", "r") as read_file:
        data = json.load(read_file)
    if type != "all":
        _return=data.get(type)
    else:
        _return=data
    print(_return)
    return _return

def do_cmd():
    loger.logger.debug("realizar os comandos")
    _return = get_data("comando")
    for cmd in _return:
        print(commandspowershell(cmd.get("cmd")))
    

def send_information():
    retur = get_data("request")
    data = "{"
    for cmd in retur:
        data += f'"{cmd.get("name")}":"{commandspowershell(cmd.get("cmd"))}",'
    data = data[:-1]
    data +="}"
    data = json.loads(data)
    return data

#testar codigos, forcando com o sistray
def do_the_cmd():
    pass

#executar os comandos em ordem se o servidor estiver on ou n
def do_all():
    estado = get_estado_con()
    if estado:
        loger.logger.info("os dados do servidor foram recebidos")
        #get_data("all")
        do_cmd()
        app_client.run_client("search")
    else:
        loger.logger.info("os dados do servidor não foram recebidos")
        get_data("all")
        do_cmd()
