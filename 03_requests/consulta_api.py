# Requests - Buscando dados na internet (API)
#
# A biblioteca requests faz o Python "acessar sites" e APIs, do mesmo jeito
# que um navegador faz quando voce abre uma pagina.
# Uma API e um endereco na web que devolve dados prontos para o programa usar,
# normalmente no formato JSON (parecido com um dicionario do Python).

import requests

# API publica e gratuita que nao precisa de senha.
url = "https://catfact.ninja/fact"

# 1. Fazendo o pedido (GET = "me manda os dados desse endereco")
resposta = requests.get(url)

# 2. O codigo de status diz se deu certo. 200 = OK.
print("Status da resposta:", resposta.status_code)

# 3. Convertendo o texto JSON da resposta em um dicionario Python
dados = resposta.json()
print("Conteudo recebido:", dados)

# 4. Pegando so o campo que interessa
print("\nCuriosidade sobre gatos:")
print(dados["fact"])

# ---------------------------------------------------------------
# Exemplo 2: enviando um parametro na URL
# A API abaixo devolve um usuario falso para testes.
# ---------------------------------------------------------------
resposta2 = requests.get("https://jsonplaceholder.typicode.com/users/1")

if resposta2.status_code == 200:
    usuario = resposta2.json()
    print("\nDados do usuario 1:")
    print("Nome:", usuario["name"])
    print("Email:", usuario["email"])
    print("Cidade:", usuario["address"]["city"])
else:
    print("Nao foi possivel buscar o usuario.")
