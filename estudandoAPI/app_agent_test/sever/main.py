from fastapi import FastAPI
import uvicorn
import app_server
import threading
from agente import  models
from agente.database import engine
from agente.routers import computador, authentication, emprestimo, impressora, user, zona, cmd,cmd_order
import loger
import time
app = FastAPI()


#criar o banco de dados
models.Base.metadata.create_all(engine)

#incluir as rotas da api
app.include_router(authentication.router)
app.include_router(computador.router)
app.include_router(user.router)
app.include_router(impressora.router)
app.include_router(zona.router)
app.include_router(emprestimo.router)
app.include_router(cmd.router)
app.include_router(cmd_order.router)


def socket_server():
    while True:
        loger.logger.info("run socket server")
        app_server.run_server()
        loger.logger.info("socket server is down")
        time.sleep(10)

#iniciar automaticamente o servidor
if __name__ == "__main__":
    threading.Thread(target=socket_server).start()
    while True:
        loger.logger.info("run fastapi server")
        uvicorn.run("main:app",host="10.2.154.25", port=8000, reload=True)
        loger.logger.info("fastapi server is down")
        time.sleep(10)


    
    

