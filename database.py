from typing import List
from models import Contato

db: List[Contato] = []
counter = 1

def next_id():
    global counter
    id_atual = counter
    counter += 1
    return id_atual
