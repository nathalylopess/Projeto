from fastapi import FastAPI,HTTPException
from typing import List
from models import Livro,Usuario,Emprestimo
import uuid
from datetime import date

acervo:List[Livro]=[]
usuarios:List[Usuario]=[]
emprestimos:List[Emprestimo]=[]

app = FastAPI()

@app.post("/livros",response_model=Livro)
def cadastrar_livro(livro:Livro):
    livro.uuid = str(uuid.uuid4())
    acervo.append(livro)
    return livro

@app.get("/livros",response_model=List[Livro])
def listar_livros():
    return acervo

@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros(titulo:str):
    for livro in acervo:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(404,"Livro não encontrado")

@app.post("/usuarios",response_model=Usuario)
def cadastrar_usuario(usuario:Usuario):
    usuario.uuid = str(uuid.uuid4())
    usuarios.append(usuario)
    return usuario

@app.post("/emprestimo",response_model=Emprestimo)
def emprestimo(usuario:str,livro:str,data_emprestimo:date,data_devolucao:date):
    user = None
    book = None
    for u in usuarios:
        print(u.uuid) 
        print(usuario) 
        print(u.uuid.strip() == usuario.strip())
        if u.uuid == usuario:
            user = u
    for l in acervo:
        if l.uuid == livro:
            if l.disponibilidade:
                book = l
    print(book and user)
    print(book )
    print( user)
    if book and user:
        book.disponibilidade=False
        dados = {
            "usuario":user,
            "livro":book,
            "emprestimo":data_emprestimo,
            "devolucao":data_devolucao
        }
        emprestimo = Emprestimo(**dados)
        emprestimos.append(emprestimo)
        return emprestimo
    raise HTTPException(404,"Emprestimo não realizado.")