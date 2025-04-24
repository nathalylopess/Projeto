from fastapi import FastAPI
from models import Tarefa
from typing import List

app = FastAPI() # a partir dele serão criadas as rotas

tarefas:List[Tarefa]=[] # tipando a variávvel para receber apenas itens desse tipo

@app.get("/tarefas/",response_model=List[Tarefa])
def listar_tarefas():
    return tarefas