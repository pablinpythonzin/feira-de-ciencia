# Selenium - Fazendo login em um site com usuario e senha
#
# ATENCAO SOBRE SEGURANCA (leia antes de rodar):
#   NUNCA escreva sua senha direto no codigo, tipo senha = "minhaSenha123".
#   Este projeto e enviado para um repositorio PUBLICO no GitHub - se a senha
#   estivesse escrita aqui, qualquer pessoa no mundo poderia ve-la e usar
#   seu login.
#
#   Por isso, o RA e a senha ficam guardados em um arquivo separado chamado
#   ".env", que existe SO no seu computador e nunca e enviado para o GitHub
#   (ele esta listado no .gitignore do projeto).
#
# Como configurar antes de rodar:
#   1. pip install selenium python-dotenv
#   2. Crie, nesta mesma pasta, um arquivo chamado ".env" com este conteudo
#      (substitua pelos seus dados reais):
#         SALA_DO_FUTURO_RA=seu_ra_aqui_sem_o_digito
#         SALA_DO_FUTURO_DIGITO=seu_digito_aqui
#         SALA_DO_FUTURO_SENHA=sua_senha_aqui
#   3. Rode este arquivo normalmente (o .env e lido automaticamente).
#
# IMPORTANTE: sites de login mudam de layout com o tempo, e o selenium
# encontra os campos pelo "placeholder" deles no HTML (o texto cinza que
# aparece dentro do campo antes de digitar), porque essa pagina e feita em
# React e os "id" dos campos sao gerados aleatoriamente a cada carregamento.
# Se der erro de "elemento nao encontrado", abra o site, aperte F12
# (Inspecionar), clique com o botao direito no campo -> Inspecionar, e ajuste
# o seletor (By.XPATH / placeholder) usado abaixo.

import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()  # le o arquivo .env e disponibiliza os valores com os.getenv()

ra = os.getenv("SALA_DO_FUTURO_RA")
digito = os.getenv("SALA_DO_FUTURO_DIGITO")
senha = os.getenv("SALA_DO_FUTURO_SENHA")

if not ra or not digito or not senha:
    raise SystemExit(
        "RA, digito ou senha nao encontrados.\n"
        "Crie um arquivo .env nesta pasta com SALA_DO_FUTURO_RA, "
        "SALA_DO_FUTURO_DIGITO e SALA_DO_FUTURO_SENHA (veja as instrucoes "
        "no topo deste arquivo)."
    )

navegador = webdriver.Chrome()
navegador.implicitly_wait(10)   # espera ate 10s por um elemento antes de desistir

try:
    # 1. Abre a pagina de login dos alunos
    navegador.get("https://saladofuturo.educacao.sp.gov.br/login-alunos")
    time.sleep(3)   # da tempo da pagina (feita em React) terminar de carregar

    # 2. Preenche o campo de RA (o primeiro campo numerico da tela)
    campo_ra = navegador.find_element(
        By.XPATH, "//label[normalize-space()='RA']/following::input[1]"
    )
    campo_ra.send_keys(ra)
    time.sleep(1)

    # 3. Preenche o campo de Digito RA (o segundo campo numerico, ao lado do RA)
    campo_digito = navegador.find_element(
        By.XPATH, "//label[contains(., 'gito')]/following::input[1]"
    )
    campo_digito.send_keys(digito)
    time.sleep(1)

    # 4. Preenche o campo de senha
    campo_senha = navegador.find_element(By.CSS_SELECTOR, "input[placeholder='Digite sua senha']")
    campo_senha.send_keys(senha)
    time.sleep(1)

    # 5. Clica no botao "Acessar" para enviar o formulario
    botao_acessar = navegador.find_element(
        By.XPATH, "//button[contains(., 'Acessar')]"
    )
    botao_acessar.click()
    time.sleep(3)   # espera a pagina seguinte (apos o login) carregar

    print("Login enviado! Titulo da pagina agora:", navegador.title)

finally:
    print("O navegador vai ficar aberto por mais 10 segundos para voce conferir...")
    time.sleep(10)
    navegador.quit()
