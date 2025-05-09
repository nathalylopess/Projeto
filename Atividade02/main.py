from fastapi import FastAPI, HTTPException
from models import Livro, Pessoa, Emprestimo, Devolucao
from typing import List

app = FastAPI() # a partir dele serão criadas as rotas

livros:List[Livro]=[] # tipando a variávvel para receber apenas itens desse tipo
pessoas:List[Pessoa]=[]
emprestimos:List[Emprestimo]=[]
devolucao:List[Devolucao]=[]

#Cadastrar um novo livro no acervo da biblioteca.
@app.post("/livros/", response_model=Livro)
def criar_livro(livro:Livro):
    livros.append(livro)
    return livro 
''' |
    |
    v
    Verificar se esse tipo que eu estou retornando é compatível com o response_model,
    se não for, vai dar o erro 500, significando que os tipos não são compatíveis.
'''

# Listar todos os livros cadastrados, incluindo seu estado de disponibilidade.
@app.get("/livros/",response_model=List[Livro])
def listar_livros():
    livros_disponiveis = [livro for livro in livros if livro.disponibilidade]
    return livros_disponiveis

#Buscar um livro específico pelo título.
@app.get("/livros/{id}",response_model=Livro)
def listar_livro(titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(status_code=404,detail="Não Localizado")

#Cadastrar um novo usuário no sistema da biblioteca.
@app.post("/pessoas/", response_model=Pessoa)
def criar_pessoa(pessoa:Pessoa):
    pessoas.append(pessoa)
    return pessoa 

#Realizar o empréstimo de um livro para um usuário
@app.post("/emprestimos/", response_model=Emprestimo)
def criar_emprestimo(emprestimo: Emprestimo):
    livro_encontrado = None
    for livro in livros:
        if livro.uuid == emprestimo.livro_uuid:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        raise HTTPException(status_code=404,detail="Não Localizado")
    
    if not livro_encontrado.disponibilidade:
        raise HTTPException(status_code=400, detail="Livro indisponível para empréstimo")

    pessoa_encontrada = None
    for pessoa in pessoas:
        if pessoa.uuid == emprestimo.pessoa_uuid:
            pessoa_encontrada = pessoa
            break

    if not pessoa_encontrada:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    # Atualizar status do livro e da pessoa
    livro_encontrado.disponibilidade = False
    pessoa_encontrada.livros_emp.append(livro_encontrado.uuid)
 
    emprestimos.append(emprestimo)

    return emprestimo

# Registrar a devolução de um livro
@app.post("/devolucao/", response_model=Devolucao)
def registrar_devolucao(devolucao_req: Devolucao):
    for pessoa in pessoas:
        if pessoa.uuid == devolucao_req.pessoa_uuid:
            pessoa = pessoa
            break
    else:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    for livro in livros:
        if livro.uuid == devolucao_req.livro_uuid:
            livro = livro
            break
    else:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    if livro.uuid not in pessoa.livros_emp:
        raise HTTPException(status_code=400, detail="Livro não está emprestado por essa pessoa")

    livro.disponibilidade = True
    pessoa.livros_emp.remove(livro.uuid)

    devolucao.append(devolucao_req)
    return devolucao_req

# Listar livros emprestados por uma pessoa
@app.get("/pessoas/{uuid}/livros_emprestados/", response_model=List[Livro])
def listar_livros_emprestados(uuid: str):
    for pessoa in pessoas:
        if pessoa.uuid == uuid:
            pessoa = pessoa
            break
    else:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    livros_emprestados = []
    for livro in livros:
        if livro.uuid in pessoa.livros_emp:
            livros_emprestados.append(livro)

    return livros_emprestados