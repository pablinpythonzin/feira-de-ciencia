# Selenium - Abrindo varias abas e visitando um site diferente em cada uma
#
# O selenium serve para automatizar um navegador de verdade: abrir paginas,
# clicar em botoes, preencher formularios... tudo isso sem voce tocar no mouse.
#
# Neste exemplo o navegador abre 5 abas, uma a cada 1 segundo, e cada aba
# visita um site diferente. As pausas (time.sleep) sao so para dar tempo
# de acompanhar o processo acontecendo na tela - sem elas, tudo aconteceria
# rapido demais para ver.
#
# Requisitos para rodar este exemplo:
#   pip install selenium
#   Ter o Google Chrome instalado no computador.
#   (o proprio selenium baixa o "driver" do Chrome automaticamente na primeira vez)

import time
from selenium import webdriver

# Cada item e uma dupla (titulo so para o print, endereco que vai ser aberto).
sites = [
    ("Preco do bitcoin", "https://www.google.com/search?q=bitcoin+preco"),
    ("Google Maps", "https://www.google.com/maps"),
    ("Site do ENEM", "https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem"),
    ("Carro esportivo", "https://www.google.com/search?q=carro+esportivo"),
    ("Python.org", "https://www.python.org"),
]

# 1. Abre uma janela do Chrome controlada pelo codigo
navegador = webdriver.Chrome()
navegador.implicitly_wait(5)   # espera ate 5s por um elemento antes de desistir

# A janela comeca com uma aba em branco. Vamos abrir uma aba nova para
# cada site da lista, sempre trocando o foco do selenium para a aba nova.
for titulo, url in sites:
    print(f"Abrindo aba: {titulo}")

    navegador.switch_to.new_window("tab")   # abre uma aba nova e ja muda o foco para ela
    navegador.get(url)

    time.sleep(1)   # intervalo de 1 segundo entre uma aba e outra

print("\nAs 5 abas foram abertas.")
print("De proposito o navegador NAO fecha sozinho, para voce conseguir ver")
print("o resultado de cada pesquisa. Feche a janela manualmente quando terminar.")

# Repare que nao chamamos navegador.quit() aqui - e isso mesmo, e proposital.
