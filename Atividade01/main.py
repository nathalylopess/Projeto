from fastapi import FastAPI, HTTPException, Request
from models import Tarefa
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI() # a partir dele serão criadas as rotas
app.mount("/static", StaticFiles(directory="static"), name="static")

tarefas:List[Tarefa]=[] # tipando a variávvel para receber apenas itens desse tipo


@app.get("/", response_class=HTMLResponse)
async def list_tarefa(request: Request):
    return templates.TemplateResponse("listarTarefa.html", {"request": request, "tarefas": tarefas})

@app.get("/cadastrar-tarefas", response_class=HTMLResponse)
async def cad_tarefa(request: Request):
    return templates.TemplateResponse("cadastrar_tarefa.html", {"request": request, "tarefas": tarefas})

@app.get("/tarefas/{id}", response_model=Tarefa)
def listar_tarefa(id:int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
        raise HTTPException(status_code=404, detail="Não encontrada")

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefas.append(tarefa)
    return tarefa 
''' |
    |
    v
    Verificar se esse tipo que eu estou retornando é compatível com o response_model,
    se não for, vai dar o erro 500, significando que os tipos não são compatíveis.
'''
   