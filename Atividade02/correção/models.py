from pydantic import BaseModel
from typing import List
from datetime import date

class Livro(BaseModel):
    uuid:str
    titulo:str
    autor:str
    ano:str
    disponibilidade:bool

class Usuario(BaseModel):
    uuid:str
    nome:str
    livros:List[Livro]

class Emprestimo(BaseModel):
    usuario:Usuario
    livro:Livro
    emprestimo:date
    devolucao:date