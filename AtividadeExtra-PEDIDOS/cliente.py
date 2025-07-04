import requests

URL = "http://127.0.0.1:8000"

def listar_pedido(IdPedido):
    r = requests.get(f"{URL}/pedidos/{IdPedido}")    
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def menu():
    print("\n")
    print("=-=-=-=-= PEDIDOS =-=-=-=-=")
    print("\n")
    print("1 - Listar Pedido pelo ID")
    print("2 - Sair")
    return int(input("\nDigite sua opção: "))

opcao = menu()

while opcao != 2:

    if opcao == 1:
        idpedido = input("Digite o ID do Pedido: ")
        listar_pedido(idpedido)

    opcao = menu()