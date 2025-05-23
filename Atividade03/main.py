from fastapi import FastAPI,HTTPException
from models import Usuario,Livro,Biblioteca,Emprestimo
from typing import List
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
usuarios:List[Usuario]=[]
livros:List[Livro]=[]
bibliotecas: List[Biblioteca] = []
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/bibliotecas",response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome ==nome:
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.post("/bibliotecas")
def cadastrar_biblioteca(nome:str):
    data = {
        "nome":nome,
        "acervo":[],
        "usuarios":[],
        "emprestimos":[]
    }
    biblioteca = Biblioteca(**data)
    bibliotecas.append(biblioteca)
    
@app.delete("/bibliotecas/{nome}",response_model=Biblioteca)
def listar_biblioteca(nome:str):
    for id,biblioteca in enumerate(bibliotecas):
        if biblioteca.nome ==nome:
            bibliotecas.pop(id)
            return biblioteca
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/",response_model=List[Usuario])
def listar_usuarios(nome:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            return biblioteca.usuarios
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/{username}", response_model=Usuario)
def listar_usuario(nome:str, username:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            for usuario in usuarios:
                if usuario.username == username:
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.post("/usuarios/")
def criar_usuario(nome:str,usuario:Usuario):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            return biblioteca.usuarios.append(usuario)
    raise HTTPException(404,"Não localizado.")
   
@app.delete("/usuarios/{username}",response_model=Usuario)
def excluir_usuario(nome:str,username:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            for id,usuario in enumerate(usuarios):
                if usuario.username == username:
                    usuarios.pop(id)
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.get("/livros",response_model=List[Livro])
def listar_livros(nome:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            return biblioteca.acervo
    raise HTTPException(404,"não localizado")  
 
@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros(nome:str, titulo:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            for livro in biblioteca.acervo:
             if livro.titulo == titulo:
                return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(nome:str,titulo:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            for id, livro in enumerate(biblioteca.acervo):
                if livro.titutlo == titulo:
                    livros.pop(id)
                    return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(nome:str,livro:Livro):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
            biblioteca.acervo.append(livro)
            return livro
    raise HTTPException(404,"Não localizado")