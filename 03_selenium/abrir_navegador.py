# Selenium - Controlando um navegador pelo codigo
#
# O selenium serve para automatizar um navegador de verdade: abrir paginas,
# clicar em botoes, preencher formularios... tudo isso sem voce tocar no mouse.
#
# Requisitos para rodar este exemplo:
#   pip install selenium
#   Ter o Google Chrome instalado no computador.
#   (o proprio selenium baixa o "driver" do Chrome automaticamente na primeira vez)

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Abre uma janela do Chrome controlada pelo codigo
navegador = webdriver.Chrome()

try:
    # 2. Manda o navegador ir ate um site
    navegador.get("https://www.python.org")

    # 3. Le informacoes da pagina que foi carregada
    print("Titulo da pagina:", navegador.title)
    print("Endereco atual:", navegador.current_url)

    # 4. Encontrando um elemento na pagina pelo nome/id
    #    Aqui pegamos a caixa de busca do site (id="id-search-field")
    caixa_busca = navegador.find_element(By.ID, "id-search-field")
    print("Encontrou a caixa de busca:", caixa_busca is not None)

    # 5. Tirando um print da tela (screenshot) para guardar como prova
    navegador.save_screenshot("pagina_python_org.png")
    print("Screenshot salvo como 'pagina_python_org.png'")

finally:
    # 6. Sempre fechar o navegador no final, mesmo se der erro no meio do caminho
    navegador.quit()
