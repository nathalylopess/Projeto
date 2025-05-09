from pydantic import BaseModel

class Tarefa(BaseModel):
    id:int
    descricao:str
    prioridade:int
    concluida:bool