from passlib.context import CryptContext

#metodo de cryptografico
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    #criptografar
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    #descriptografar
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)