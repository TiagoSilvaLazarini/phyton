import json
from cryptography.fernet import Fernet

def save_key(key):
    with open("key.key", "wb") as key_file: 
        key_file.write(key) 

def load_key():
    return open("key.key", "rb").read()

def encrypt_data(data):
    f=Fernet(load_key())
    return f.encrypt(data)
    

def decrypt_data(data):
    f=Fernet(load_key())
    return f.decrypt(data)
    