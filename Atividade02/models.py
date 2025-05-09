from pydantic import BaseModel

class Livro(BaseModel):
    uuid:str
    titulo:str
    autor:str
    ano_pub:int
    disponibilidade:bool = True

class Pessoa(BaseModel):
    uuid:str
    nome:str
    livros_emp: list[str] = []

class Emprestimo(BaseModel):
    id: str  
    livro_uuid: str
    pessoa_uuid: str
    data_emprestimo: str  
    data_devolucao: str | None = None 

class Devolucao(BaseModel):
    pessoa_uuid:str
    livro_uuid:str
    data_devolucao:str
