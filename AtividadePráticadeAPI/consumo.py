#pip install requests
import requests

URL = "http://127.0.0.1:8000"


def listar_livros():
    r = requests.get(f"{URL}/livros")    
    if r.status_code == 200:
        print(r.text)

def cadastrar_livro():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a Edição:"))
    livro = {
        "titulo":titulo,
        "ano":ano,
        "edicao":edicao
    }
    r = requests.post(f"{URL}/livros", json=livro)

def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")    
    if r.status_code == 200: # oq é essa variável status_code e de onde ela vem
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print("Excluiído com sucesso")
    else:
        print(r.text)

def editar_livro(aux):
    titulo = input("Digite o novo título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a Edição:"))
    livro = {
        "titulo":titulo,
        "ano":ano,
        "edicao":edicao
    }
    r = requests.put(f"{URL}/livros/{aux}", json=livro)  
    

def menu():
    print("\n")
    print("1 - Listar Livos")
    print("2 - Listar Livros pelo Título")
    print("3 - Cadastrar Livro")
    print("4 - Editar Livro")
    print("5 - Deletar Livro")
    print("6 - Sair")
    return int(input("\nDigite sua opção: "))

opcao = menu()

while opcao != 6:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = input("Digite o título: ")
        listar_livro(titulo)
    elif opcao == 3:
        cadastrar_livro()
    elif opcao == 4:
        aux = input("Digite o título: ")
        editar_livro(aux)
    elif opcao == 5:
        titulo = input("Digite o título: ")
        excluir_livro(titulo)
    opcao = menu()
