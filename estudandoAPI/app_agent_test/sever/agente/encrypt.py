from cryptography.fernet import Fernet

def generate_key():
    f =Fernet.generate_key()
    return f.decode("utf-8")


def encrypt_data(data,key):
    f=Fernet(key)
    return f.encrypt(data)
    

def decrypt_data(data,key):
    f=Fernet(key)
    return f.decrypt(data)
    