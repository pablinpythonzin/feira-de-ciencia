# Matplotlib - Histograma e comparacao de medias escolares por turma
#
# Aqui usamos o modulo 'random' so para gerar notas de exemplo.
# A ideia e mostrar como visualizar a distribuicao de uma nota (histograma)
# e como comparar varios grupos entre si (grafico de barras).

import random
import matplotlib.pyplot as plt

turmas = ["3°A", "3°B", "2°A", "2°B", "1°A", "1°B"]
ALUNOS_POR_TURMA = 30

# ---------------------------------------------------------------
# Gerando as medias escolares de cada aluno, turma por turma.
# random.gauss(7, 1.5) sorteia numeros em torno de 7, com variacao de 1.5.
# ---------------------------------------------------------------
medias_por_turma = {}
todas_as_medias = []

for turma in turmas:
    notas_da_turma = [
        max(0, min(10, random.gauss(7, 1.5)))   # garante que a nota fique entre 0 e 10
        for _ in range(ALUNOS_POR_TURMA)
    ]
    medias_por_turma[turma] = sum(notas_da_turma) / len(notas_da_turma)
    todas_as_medias.extend(notas_da_turma)

# ---------------------------------------------------------------
# HISTOGRAMA: mostra como as medias escolares estao distribuidas
# considerando todos os alunos das 6 turmas juntos.
# ---------------------------------------------------------------
plt.figure()
plt.hist(todas_as_medias, bins=15, color="steelblue", edgecolor="black")
plt.title("Distribuicao das medias escolares (todas as turmas)")
plt.xlabel("Media escolar")
plt.ylabel("Quantidade de alunos")
plt.savefig("histograma_medias.png")
print("histograma_medias.png criado.")

# ---------------------------------------------------------------
# BARRAS: compara a media de cada turma entre si.
# ---------------------------------------------------------------
plt.figure()
plt.bar(medias_por_turma.keys(), medias_por_turma.values(), color="green")
plt.title("Media escolar por turma")
plt.xlabel("Turma")
plt.ylabel("Media")
plt.ylim(0, 10)
plt.savefig("media_por_turma.png")
print("media_por_turma.png criado.")

# plt.show()  # descomente para ver os graficos na tela
