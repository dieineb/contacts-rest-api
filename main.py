from fastapi import FastAPI, HTTPException
from models import Contato, ContatoCreate
from database import db, next_id

app = FastAPI(title="API de Agenda de Contatos")

@app.post("/contatos/", response_model=Contato)
def criar_contato(contato: ContatoCreate):
    id_atual = next_id()
    novo_contato = Contato(id=id_atual, **contato.dict())
    db.append(novo_contato)
    return novo_contato

@app.get("/contatos/", response_model=list[Contato])
def listar_contatos():
    return db

@app.get("/contatos/{id}", response_model=Contato)
def buscar_contato(id: int):
    for contato in db:
        if contato.id == id:
            return contato
    raise HTTPException(status_code=404, detail="Contato não encontrado")
