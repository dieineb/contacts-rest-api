from pydantic import BaseModel
from typing import List, Literal


class Telefone(BaseModel):
    numero: str
    tipo: Literal['movel', 'fixo', 'comercial']


class ContatoCreate(BaseModel):
    nome: str
    telefones: List[Telefone]
    categoria: Literal['familiar', 'pessoal', 'comercial']


class Contato(ContatoCreate):
    id: int
