# Selenium - Preenchendo um formulario e clicando em botoes
#
# Aqui a ideia e simular o que uma pessoa faria: digitar algo em uma caixa
# de busca e apertar Enter (ou clicar no botao), depois ler o resultado.
#
# Requisitos: pip install selenium  +  Google Chrome instalado.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

try:
    # 1. Abre o site da Wikipedia em portugues
    navegador.get("https://pt.wikipedia.org")

    # 2. Encontra a caixa de pesquisa pelo nome do campo (atributo "name")
    campo_busca = navegador.find_element(By.NAME, "search")

    # 3. Digita um termo de pesquisa, como se fosse um usuario digitando
    campo_busca.send_keys("Feira de ciencias")

    # 4. Aperta Enter para pesquisar (poderia tambem clicar em um botao)
    campo_busca.send_keys(Keys.ENTER)

    # 5. Da um tempinho para a nova pagina carregar
    time.sleep(2)

    # 6. Le o titulo da pagina de resultado
    print("Titulo da pagina depois da busca:", navegador.title)

    # 7. Pega o primeiro paragrafo do artigo, se existir
    paragrafos = navegador.find_elements(By.CSS_SELECTOR, "p")
    for paragrafo in paragrafos:
        texto = paragrafo.text.strip()
        if texto:
            print("\nPrimeiro paragrafo encontrado:")
            print(texto)
            break

finally:
    navegador.quit()
