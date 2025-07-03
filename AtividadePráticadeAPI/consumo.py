#pip install requests

import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    r = requests.get(f"{url}/livros")
    print(r.text)
    livro = {
        "titulo": "Python como Programar",
        "ano": 2024,
        "edicao": 1
    }
    r = requests.post(f"{url}/livros",json=livro)
    print(r.status_code)
    print(r.text)
    pesquisa = "Python como Programar"
    r = requests.get(f"{url}/livros/{pesquisa}")
    print(r.status_code)
    print(r.text)
    r = requests.delete(f"{url}/livros/{pesquisa}")
    print(r.status_code)