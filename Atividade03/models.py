from pydantic import BaseModel
from datetime import date
from typing import List

class Usuario(BaseModel):
    username:str
    password:str
    data_criacao:date

class Livro(BaseModel):
    titulo:str
    ano:int
    edicao:int

class Emprestimo(BaseModel):
    usuario:Usuario
    livro:Livro
    data_emprestimo:date
    data_devolucao:date


class Biblioteca(BaseModel):
    nome:str
    acervo: List[Livro]
    usuarios: List[Usuario]
    emprestimos: List[Emprestimo]