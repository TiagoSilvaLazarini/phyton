from imp import reload
from fastapi import FastAPI
import uvicorn
from agente import  models
from agente.database import engine
from agente.routers import computador, authentication, emprestimo, impressora, user, zona

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

if __name__ == "__main__":
    uvicorn.run("main:app",host="10.2.154.25", port=8000, reload=True)
