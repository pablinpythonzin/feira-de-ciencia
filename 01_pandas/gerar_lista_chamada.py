# Pandas - Gerando uma planilha (Excel) com varias abas
#
# Objetivo: simular a lista de chamada de uma sessao de aula.
# Cada turma vira uma ABA diferente dentro do mesmo arquivo .xlsx,
# com as colunas ID, NOME e STATUS (Presente ou Faltou).
#
# Para o pandas conseguir salvar em .xlsx, e preciso instalar o openpyxl:
#   pip install openpyxl

import random
import pandas as pd

# Turmas que vao virar as abas da planilha
turmas = ["3°A", "3°B", "2°A", "2°B", "1°A", "1°B"]

ALUNOS_POR_TURMA = 30


def gerar_turma(turma: str) -> pd.DataFrame:
    """Cria a tabela de uma turma: ID, NOME e STATUS de presenca."""
    ids = list(range(1, ALUNOS_POR_TURMA + 1))
    nomes = [f"Aluno {numero}" for numero in ids]
    # Sorteia a presenca de cada aluno (80% de chance de estar presente)
    status = [random.choices(["Presente", "Faltou"], weights=[80, 20])[0] for _ in ids]

    return pd.DataFrame({
        "ID": ids,
        "NOME": nomes,
        "STATUS": status,
    })


# 1. Cria o arquivo Excel e vai escrevendo uma aba para cada turma
nome_arquivo = "lista_chamada.xlsx"

with pd.ExcelWriter(nome_arquivo, engine="openpyxl") as escritor:
    for turma in turmas:
        tabela_turma = gerar_turma(turma)
        # sheet_name e o nome da aba dentro do Excel
        tabela_turma.to_excel(escritor, sheet_name=turma, index=False)

print(f"Planilha '{nome_arquivo}' criada com {len(turmas)} abas: {', '.join(turmas)}")

# 2. Reabrindo o arquivo para mostrar que deu certo (le todas as abas de volta)
todas_as_abas = pd.read_excel(nome_arquivo, sheet_name=None)  # sheet_name=None le todas as abas

print("\nResumo de faltas por turma:")
for turma, tabela in todas_as_abas.items():
    faltas = (tabela["STATUS"] == "Faltou").sum()
    presentes = (tabela["STATUS"] == "Presente").sum()
    print(f"  {turma}: {presentes} presentes / {faltas} faltas (de {len(tabela)} alunos)")
