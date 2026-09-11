# Matplotlib - Criando graficos basicos
#
# O matplotlib transforma listas de numeros em graficos (imagens).
# O modulo mais usado e o "pyplot", que costuma ser apelidado de plt.

import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# GRAFICO 1: linha (bom para mostrar evolucao ao longo do tempo)
# ---------------------------------------------------------------
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
visitantes = [120, 150, 90, 200, 240]

plt.figure()                      # cria uma janela/figura nova
plt.plot(meses, visitantes, marker="o")   # marker="o" coloca uma bolinha em cada ponto
plt.title("Visitantes por mes")
plt.xlabel("Mes")
plt.ylabel("Numero de visitantes")
plt.grid(True)                     # linhas de fundo para ajudar a leitura
plt.savefig("grafico_linha.png")  # salva a imagem em um arquivo
print("grafico_linha.png criado.")

# ---------------------------------------------------------------
# GRAFICO 2: barras (bom para comparar categorias)
# ---------------------------------------------------------------
frutas = ["Maca", "Banana", "Uva", "Manga"]
vendas = [30, 55, 20, 40]

plt.figure()
plt.bar(frutas, vendas, color="orange")
plt.title("Frutas vendidas")
plt.ylabel("Quantidade")
plt.savefig("grafico_barras.png")
print("grafico_barras.png criado.")

# ---------------------------------------------------------------
# GRAFICO 3: pizza (bom para mostrar partes de um todo, em %)
# ---------------------------------------------------------------
linguagens = ["Python", "JavaScript", "C", "Outras"]
uso = [50, 25, 15, 10]

plt.figure()
plt.pie(uso, labels=linguagens, autopct="%1.1f%%")  # autopct escreve a porcentagem
plt.title("Uso de linguagens na turma")
plt.savefig("grafico_pizza.png")
print("grafico_pizza.png criado.")

# plt.show() abre as janelas dos graficos na tela.
# Deixe descomentado se quiser ver os graficos ao inves de so salvar.
# plt.show()
