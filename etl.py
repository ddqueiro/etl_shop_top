# -*- coding: utf-8 -*-
"""Dannyelly Queiroz - DECISÕES BASEADAS EM DADOS

Original file is located at
    https://colab.research.google.com/drive/1Qffk_p3MIRnaodfgeWAZkHj_RGp8KSLA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from datetime import datetime
from google.colab import files

"""#Lendo os dados"""

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSZ00L6MPCKsagqr2M5hjoHi58lH0S5r0VwRyn6Dp-ntvgQKHLoebKZSGr62W7mrBTS6x_QbSraWZYP/pub?gid=540741118&single=true&output=csv')

display(df)

"""#Identificar e tratar possíveis inconsistências nos dados, como valores nulos ou duplicados.

##Verificando o tipo de dados
"""

df.info()

"""##Alterando o tipo de dados"""

df['Date'] = pd.to_datetime(df['Date'])
df['TransactionID'] = df['TransactionID'].astype(str)

"""## Comando describe"""

(round(df[["Price", "Discount", "Quantity"]].describe(),2))

"""##Verificando se tem dados nulos"""

print(df.isnull().sum())
nulos = df.isnull().sum()
if nulos.sum() > 0:
  nulos.dropna(inplace=True)
  print(f"Tem dados nulos, tem {nulos} linhas nulas ")
else:
  print('Não tem dados nulos')

"""##Verificando se tem dados duplicados"""

duplicadas = df.duplicated().sum()
if duplicadas > 0:
    df.drop_duplicates(inplace=True)
    print(f"Tem dados duplicados, tem {duplicadas} linhas duplicadas")
else:
    print(f"Não tem dados duplicados")

"""#Estatisticas

##Média, moda e mediana
"""

##Média
media_preco= df['Price'].mean()
media_quant= df['Quantity'].mean()
media_desc= df['Discount'].mean()
print(f'A média do preço é {media_preco}')
print(f'A média da quantidade é {media_quant}')
print(f'A média do desconto é {media_desc}')
print('----------------------------------------')
#moda
moda_preco= df['Price'].mode()[0]
moda_quant= df['Quantity'].mode()[0]
moda_desc= df['Discount'].mode()[0]
print(f'A moda do preço é {moda_preco}')
print(f'A moda da quantidade é {moda_quant}')
print(f'A moda do desconto é {moda_desc}')
print('----------------------------------------')
#mediana
mediana_preco= df['Price'].median()
mediana_quant= df['Quantity'].median()
mediana_desc= df['Discount'].median()
print(f'A mediana do preço é {mediana_preco}')
print(f'A mediana da quantidade é {mediana_quant}')
print(f'A mediana do desconto é {mediana_desc}')

"""##Verificando os Quartis"""

Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

# Definindo os limites inferior e superior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1 (1º quartil): {Q1}")
print(f"Q3 (3º quartil): {Q3}")
print(f"IQR (Intervalo Interquartílico): {IQR}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")

Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1

# Definindo os limites inferior e superior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1 (1º quartil): {Q1}")
print(f"Q3 (3º quartil): {Q3}")
print(f"IQR (Intervalo Interquartílico): {IQR}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")

Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1

# Definindo os limites inferior e superior
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1 (1º quartil): {Q1}")
print(f"Q3 (3º quartil): {Q3}")
print(f"IQR (Intervalo Interquartílico): {IQR}")
print(f"Limite Inferior: {limite_inferior}")
print(f"Limite Superior: {limite_superior}")

# Função para calcular os limites inferior e superior com base no IQR
def calcular_limites(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return limite_inferior, limite_superior

# Função para detectar outliers
def detectar_outliers(df, colunas):
    outliers = pd.DataFrame()

    # Iterando por cada coluna para calcular limites e detectar outliers
    for coluna in colunas:
        limite_inferior, limite_superior = calcular_limites(df, coluna)

        # Detectando outliers com base nos limites calculados
        outliers_coluna = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]

        # Adicionando os outliers encontrados ao DataFrame final
        outliers = pd.concat([outliers, outliers_coluna])


    # Retornando as colunas de interesse
    return outliers[['Price', 'Discount', 'Quantity']]

colunas_para_checar = ['Price', 'Discount', 'Quantity']

outliers = detectar_outliers(df, colunas_para_checar)

# Exibindo os outliers encontrados
print("Outliers encontrados:")
print(outliers)

"""##Correlação dos dados"""

# Selecionar apenas as colunas numéricas
df_numero = df.select_dtypes(include=['float64', 'int64'])
correlacoes = round(df_numero.corr(),2)
display(correlacoes)

"""###Gráfico de correlação"""

#Selecionando apenas as colunas numéricas
df_numerico = df.select_dtypes(include=['float64', 'int64'])

# Gerar o heatmap da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
# Exibir o gráfico
plt.title('Matriz de Correlação')
plt.show()

"""#Perguntas

##1 - Quais são os produtos mais vendidos por categoria?
"""

#Quais são os produtos mais vendidos por categoria?
df_soma = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
df_soma = df_soma.sort_values(by=["Category", "Quantity"], ascending=[True, False])  # Ordena por categoria e quantidade
df_soma
df_maisvendido = df_soma.loc[df_soma.groupby("Category")["Quantity"].idxmax()]
display(df_maisvendido)

"""###gráfico para ver os produtos mais vendidos por categoria




"""

plt.figure(figsize=(10, 8))
a= sns.barplot(x="Quantity", y="Category", data=df_soma, hue="Product", palette="viridis")

for container in a.containers:
    a.bar_label(container, fmt="%.0f", padding=3)  # "%.0f" remove as casas decimais

# Adicionar títulos e rótulos
plt.xlabel("Quantidade Vendida")
plt.ylabel("Categoria")
plt.title("Produtos Mais Vendidos por Categoria")
plt.legend(title="Produto")
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Exibir o gráfico
plt.show()



"""##2. Em quais regiões as vendas foram mais expressivas?


"""

#2. Em quais regiões as vendas foram mais expressivas?
desconto = df['Discount'] = df['Discount'] / 100
df_desconto = df['Faturamento'] = df['Price'] * df['Quantity']* (1 - desconto)
regioes = df.groupby('Region')['Faturamento'].sum().reset_index()
regioes = regioes.sort_values(by="Faturamento", ascending=False)
display (round(regioes),2)

"""###gráfico para ver quais as regiões que estão com as vendas mais expressivas"""

# Ajustando a coluna 'Discount' para trabalhar corretamente
df['Discount'] = df['Discount'] / 100  # Garantir que o desconto esteja entre 0 e 1

# Calculando o faturamento por linha: Faturamento = Preço * Quantidade * (1 - Desconto)
df['Faturamento'] = df['Price'] * df['Quantity'] * (1 - df['Discount'])

# Agrupando os dados por região e somando o faturamento
regioes = df.groupby('Region')['Faturamento'].sum().reset_index()

# Ordenando os valores de faturamento em ordem decrescente
regioes = regioes.sort_values(by="Faturamento", ascending=False)
# Definindo valores mínimo e máximo para o gráfico de mapa de calor
vmin = regioes['Faturamento'].min()  # Valor mínimo de faturamento
vmax = regioes['Faturamento'].max()  # Valor máximo de faturamento
# Criando o mapa de calor
# Para o gráfico de mapa de calor, precisamos converter os dados dde faturamento por região para uma matriz 2D
faturamento_matrix = regioes['Faturamento'].values.reshape(1, -1)  # Matriz 1xN para mapa de calor

# Plotando o mapa de calor
plt.figure(figsize=(12, 2))  # Ajuste do tamanho do gráfico
sns.heatmap(faturamento_matrix, cmap="Reds", annot=True, cbar=True, xticklabels=regioes['Region'],fmt='.2f',vmin=vmin, vmax=vmax)

# Ajuste do gráfico
plt.title('Mapa de Calor do Faturamento por Região')
plt.xlabel('Região')
plt.ylabel('Faturamento')

# Exibindo o gráfico
plt.show()

"""##3. Existe relação entre os descontos e o aumento de vendas?


"""

# Agrupar os dados pela taxa de desconto e somar a quantidade vendida
#df['semporcento'] = df['Discount'] / 100
df['Faturamento'] = df['Price'] * df['Quantity']* (1 - df['Discount'])
df_desconto = df.groupby("Discount")["Quantity"].sum().reset_index()
df_desconto = df_desconto.sort_values(by="Discount", ascending=False)
df_desconto = df.groupby("Discount")["Quantity"].sum().reset_index()
df_desconto = df_desconto.sort_values(by="Discount", ascending=True)
display(df_desconto)

"""###Gráfico para a quantidade de produtos por desconto"""

df['Faturamento'] = df['Price'] * df['Quantity'] * (1 - df['Discount'])

df_desconto = df.groupby("Discount")["Quantity"].sum().reset_index()


df_desconto = df_desconto.sort_values(by="Discount", ascending=False)

plt.figure(figsize=(10, 6))
a = sns.barplot(x="Discount", y="Quantity", data=df_desconto, hue="Discount", palette='Blues_d', legend=False)

for p in a.patches:
    a.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                fontsize=12, color='black',
                xytext=(0, 5), textcoords='offset points')

sns.barplot(x="Discount", y="Quantity", data=df_desconto, hue="Discount", palette='Blues_d', legend=False)

plt.title("Quantidade de Produtos por Desconto", fontsize=16)
plt.xlabel("Desconto em Porcentagem", fontsize=14)
plt.ylabel("Quantidade Total", fontsize=14)

plt.show()

#Produtos mais vendidos de acordo com o desconto
import pandas as pd

# Agrupar os dados por desconto e produto, somar as quantidades
produtos_por_desconto = df.groupby(['Discount', 'Category'])['Quantity'].sum().reset_index()

# Ordenar os produtos dentro de cada desconto, do maior para o menor
produtos_por_desconto = produtos_por_desconto.sort_values(by=['Category', 'Quantity'], ascending=[True, False])

# Exibir os produtos mais vendidos por desconto
display(produtos_por_desconto)

"""##4. Quais dias da semana possuem maior volume de vendas?"""

#4. Quais dias da semana possuem maior volume de vendas?

df['DiaSemana'] = df['Date'].dt.day_name()
df_dia = df.groupby('DiaSemana')['Quantity'].sum().reset_index()
df_dia = df_dia.sort_values(by='Quantity', ascending=False)

display(df_dia)

"""###Gráfico dias da semana com maior volume de vendas"""

vendas_por_dia = df.groupby('DiaSemana')['Quantity'].sum().sort_values(ascending=False)
a = vendas_por_dia.plot(kind='bar')
for p in a.patches:
    a.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                fontsize=12, color='black',
                xytext=(0, 5), textcoords='offset points')
plt.title("Vendas por Dia da Semana")
plt.ylabel("Quantidade Vendida")
plt.xlabel("Dia da Semana")
plt.show()

"""##5. Qual dia da semana tem o maior faturamento?"""

df['semporcento'] = df['Discount'] / 100
df['Faturamento'] = df['Price'] * df['Quantity'] * (1 - df['semporcento'])
df['DiaSemana'] = df['Date'].dt.day_name()
fat_dia = df.groupby('DiaSemana')['Faturamento'].sum().reset_index()
fat_dia = fat_dia.sort_values(by='Faturamento', ascending=False)
display (round(fat_dia),2)

"""###Gráfico faturamento por dia da semana

"""

import matplotlib.pyplot as plt
import seaborn as sns
df['DiaSemana'] = df['Date'].dt.day_name()
fat_dia = df.groupby('DiaSemana')['Faturamento'].sum().reset_index()
fat_dia = fat_dia.sort_values(by='Faturamento', ascending=False)

fat_dia = fat_dia.set_index('DiaSemana').reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

plt.figure(figsize=(10,3))
ax = sns.lineplot(x='DiaSemana', y='Faturamento', data=fat_dia, marker='o', color='b')

for i, value in enumerate(fat_dia['Faturamento']):
    ax.annotate(f'{value:.2f}', (i, value), textcoords="offset points", xytext=(5,5), ha='center', fontsize=10)

plt.title('Faturamento por Dia da Semana')
plt.ylabel('Faturamento (em R$)')
plt.xlabel('Dia da Semana')

plt.grid(True)
plt.show()