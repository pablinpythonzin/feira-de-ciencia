# Requests - Baixando um arquivo (imagem) da internet
#
# Alem de textos e JSON, o requests tambem baixa arquivos: imagens, PDFs, musicas...
# A diferenca e que arquivos nao sao texto, entao usamos 'resposta.content' (bytes)
# e salvamos com o modo "wb" (write binary).

import requests

# Endereco de uma imagem qualquer (aqui usamos um gerador de imagem de exemplo).
url_imagem = "https://picsum.photos/400/300"

print("Baixando imagem...")
resposta = requests.get(url_imagem)

# Verifica se deu tudo certo; lanca erro se o status for 4xx ou 5xx.
resposta.raise_for_status()

# Salva os bytes recebidos em um arquivo no computador.
with open("imagem_baixada.jpg", "wb") as arquivo:
    arquivo.write(resposta.content)

# 'headers' traz informacoes extras sobre a resposta.
print("Tipo do arquivo:", resposta.headers.get("Content-Type"))
print("Tamanho:", len(resposta.content), "bytes")
print("Imagem salva como 'imagem_baixada.jpg'")

# ---------------------------------------------------------------
# Dica: sempre use timeout para o programa nao travar para sempre
# caso a internet caia no meio do download.
# ---------------------------------------------------------------
try:
    teste = requests.get("https://httpbin.org/delay/1", timeout=5)
    print("\nRequisicao com timeout funcionou. Status:", teste.status_code)
except requests.exceptions.Timeout:
    print("\nA requisicao demorou demais e foi cancelada.")
