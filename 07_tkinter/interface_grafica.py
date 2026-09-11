# Tkinter - Criando uma janela com botao e campo de texto
#
# O tkinter ja vem instalado com o Python e serve para criar programas com
# janelas, botoes, caixas de texto etc. (interface grafica, ou "GUI").
#
# Ideia geral:
#   1. Cria a janela principal
#   2. Coloca os elementos (widgets): rotulos, campos, botoes
#   3. Liga cada botao a uma funcao
#   4. Chama mainloop() para a janela ficar aberta esperando o usuario

import tkinter as tk

# 1. Janela principal
janela = tk.Tk()
janela.title("Meu primeiro programa com janela")
janela.geometry("300x200")   # largura x altura em pixels


# 3. Funcao que sera executada quando o botao for clicado
def cumprimentar():
    nome = campo_nome.get()          # pega o texto digitado no campo
    if nome.strip() == "":
        resultado.config(text="Digite seu nome primeiro!")
    else:
        resultado.config(text=f"Ola, {nome}! Bem-vindo(a).")


# 2. Widgets
rotulo = tk.Label(janela, text="Qual e o seu nome?")
rotulo.pack(pady=10)

campo_nome = tk.Entry(janela)
campo_nome.pack()

botao = tk.Button(janela, text="Cumprimentar", command=cumprimentar)
botao.pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

# 4. Mantem a janela aberta
janela.mainloop()
