# Tkinter - Mini calculadora de soma
#
# Exemplo um pouco maior: dois campos para numeros, quatro botoes de operacao
# e um lugar para mostrar o resultado.
#
# Aqui usamos o gerenciador de layout 'grid', que organiza os widgets em
# linhas e colunas (como uma tabela).

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Calculadora simples")


def calcular(operacao):
    # Tenta transformar o texto dos campos em numero.
    try:
        a = float(campo_a.get())
        b = float(campo_b.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite numeros validos nos dois campos.")
        return

    if operacao == "+":
        r = a + b
    elif operacao == "-":
        r = a - b
    elif operacao == "*":
        r = a * b
    elif operacao == "/":
        if b == 0:
            messagebox.showerror("Erro", "Nao da para dividir por zero.")
            return
        r = a / b

    label_resultado.config(text=f"Resultado: {r:g}")


# Campos de entrada
tk.Label(janela, text="Numero A:").grid(row=0, column=0, padx=5, pady=5)
campo_a = tk.Entry(janela)
campo_a.grid(row=0, column=1, columnspan=3, padx=5)

tk.Label(janela, text="Numero B:").grid(row=1, column=0, padx=5, pady=5)
campo_b = tk.Entry(janela)
campo_b.grid(row=1, column=1, columnspan=3, padx=5)

# Botoes de operacao
tk.Button(janela, text="+", width=5, command=lambda: calcular("+")).grid(row=2, column=0, pady=10)
tk.Button(janela, text="-", width=5, command=lambda: calcular("-")).grid(row=2, column=1)
tk.Button(janela, text="*", width=5, command=lambda: calcular("*")).grid(row=2, column=2)
tk.Button(janela, text="/", width=5, command=lambda: calcular("/")).grid(row=2, column=3)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.grid(row=3, column=0, columnspan=4, pady=10)

janela.mainloop()
