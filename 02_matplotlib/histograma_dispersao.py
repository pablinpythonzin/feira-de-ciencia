# Matplotlib - Histograma e grafico de dispersao
#
# Aqui usamos o modulo 'random' so para gerar numeros de exemplo.
# A ideia e mostrar mais dois tipos de grafico muito usados em analise de dados.

import random
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# HISTOGRAMA: mostra como os valores estao distribuidos.
# Exemplo: alturas (em cm) de 200 pessoas, sorteadas em torno de 170.
# ---------------------------------------------------------------
alturas = [random.gauss(170, 8) for _ in range(200)]

plt.figure()
plt.hist(alturas, bins=15, color="steelblue", edgecolor="black")
plt.title("Distribuicao de alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Quantidade de pessoas")
plt.savefig("histograma.png")
print("histograma.png criado.")

# ---------------------------------------------------------------
# DISPERSAO (scatter): mostra a relacao entre duas medidas.
# Exemplo: quanto mais horas de estudo, maior tende a ser a nota.
# ---------------------------------------------------------------
horas_estudo = [random.uniform(0, 10) for _ in range(50)]
# a nota depende das horas + um pouco de "sorte" (ruido)
notas = [min(10, h * 0.8 + random.uniform(-1, 2)) for h in horas_estudo]

plt.figure()
plt.scatter(horas_estudo, notas, color="green")
plt.title("Horas de estudo x Nota")
plt.xlabel("Horas de estudo")
plt.ylabel("Nota na prova")
plt.grid(True)
plt.savefig("dispersao.png")
print("dispersao.png criado.")

# plt.show()  # descomente para ver os graficos na tela
