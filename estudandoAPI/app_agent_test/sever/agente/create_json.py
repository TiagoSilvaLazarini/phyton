from agente import schemas, database, models, oauth2



def try_t():
    with database.SessionLocal() as session:
        result = session.query(models.CMD.id, models.CMD.comando).order_by(models.CMD.id.asc()).all()

    lista = []
    for row in result:
        lista.append({"id":row[0],"cmd":row[1]})
    return lista
