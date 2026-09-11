# Pandas - Lendo e resumindo dados de um arquivo CSV
#
# Na vida real os dados quase nunca sao digitados na mao: eles vem de um arquivo.
# O formato mais comum e o CSV (valores separados por virgula).
# Neste exemplo o proprio codigo cria o arquivo e depois le ele de volta.

import pandas as pd

# 1. Montando um pequeno CSV so para o exemplo funcionar sozinho.
#    Cada linha e um aluno; as colunas sao separadas por virgula.
conteudo_csv = """nome,turma,nota
Ana,A,8.5
Bruno,A,6.0
Carla,B,9.2
Diego,B,4.5
Eva,A,7.0
Felipe,B,5.5
"""

with open("notas.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_csv)

# 2. Lendo o CSV para dentro de um DataFrame
df = pd.read_csv("notas.csv")

print("Dados lidos do arquivo:")
print(df)

# 3. Espiando a tabela
print("\nPrimeiras linhas (head):")
print(df.head(3))

print("\nResumo estatistico das colunas numericas (describe):")
print(df["nota"].describe())

# 4. Agrupando: media de nota por turma
media_por_turma = df.groupby("turma")["nota"].mean()
print("\nMedia de nota por turma:")
print(media_por_turma)

# 5. Criando uma coluna de situacao com base na nota
df["situacao"] = df["nota"].apply(lambda n: "Aprovado" if n >= 6 else "Reprovado")
print("\nTabela com a situacao de cada aluno:")
print(df)

# 6. Salvando o resultado final em um novo CSV
df.to_csv("resultado_final.csv", index=False)
print("\nArquivo 'resultado_final.csv' salvo com sucesso.")
