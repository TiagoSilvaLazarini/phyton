from crypt import crypt
import subprocess
import json
import loger

from codigo import encrypt
# Comandos powershell
def commandspowershell(item):
    target= "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    return subprocess.getoutput([target, item])

key = b'pT8ZDjwCvnWkfPEYBm12q2p9srNkM-nWC6Ss9aAcMEw='
# Data e hora do inicio da ultima linha de execução
def dateandhour():
    return commandspowershell("(get-date).ToString()")

def save_data(data):
    print("the DATA",data)
    encrypt.save_key(key)
    encypted_data = encrypt.encrypt_data(data)

    with open("./cliente/codigo/data_file.json", "wb") as f:
        f.write(encypted_data)


def get_data():
    with open("./cliente/codigo/data_file.json", "rb") as f:
        data = f.read()
    data_dey = encrypt.decrypt_data(data)
    _return=data_dey.get("list")
    print(_return)

def do_cmd():
    with open("./cliente/codigo/data_file.json", "rb") as f:
        data = f.read()
    data_dey = encrypt.decrypt_data(data)
    _return=data_dey.get("comando")
    for cmd in _return:
        print(commandspowershell(cmd.get("cmd")))
    

def do_all():
    loger.logger.debug("get data") 
    get_data()
    loger.logger.debug("do the cmds")
    do_cmd()