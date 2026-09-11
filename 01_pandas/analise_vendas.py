# Pandas - Analisando uma tabela de vendas
#
# O pandas serve para trabalhar com dados em formato de tabela (linhas e colunas),
# parecido com uma planilha do Excel, mas usando codigo.

import pandas as pd

# 1. Criando a tabela (no pandas ela se chama "DataFrame")
#    Cada chave do dicionario vira uma coluna.
dados = {
    "produto": ["Caneta", "Caderno", "Mochila", "Lapis", "Borracha"],
    "preco": [2.50, 15.00, 89.90, 1.20, 0.80],
    "quantidade": [40, 12, 5, 60, 30],
}

df = pd.DataFrame(dados)

print("Tabela completa:")
print(df)

# 2. Criando uma coluna nova a partir de outras
#    Aqui o pandas multiplica as duas colunas linha por linha automaticamente.
df["total"] = df["preco"] * df["quantidade"]

print("\nTabela com a coluna 'total':")
print(df)

# 3. Perguntas simples sobre os dados
print("\nFaturamento total: R$", df["total"].sum())
print("Preco medio dos produtos: R$", round(df["preco"].mean(), 2))
print("Produto mais caro:", df.loc[df["preco"].idxmax(), "produto"])

# 4. Filtrando linhas (so os produtos que custam menos de R$ 10)
baratos = df[df["preco"] < 10]
print("\nProdutos que custam menos de R$ 10:")
print(baratos)

# 5. Ordenando a tabela pelo total vendido, do maior para o menor
mais_vendidos = df.sort_values("total", ascending=False)
print("\nProdutos ordenados por faturamento:")
print(mais_vendidos)
