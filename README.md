# Análise de Dados de Vendas - DECISÕES BASEADAS EM DADOS

Este projeto visa realizar uma análise de dados de vendas utilizando Python, Pandas, Seaborn e outras bibliotecas para explorar, visualizar e responder perguntas importantes sobre os dados de vendas. A análise é realizada com base em um conjunto de dados sobre produtos, categorias, preços, descontos e vendas. O código foi desenvolvido e executado no Google Colab.

## Conteúdo do Repositório

O repositório contém os seguintes arquivos e scripts:

- **Código de Análise de Dados**: Um script Python que carrega os dados, trata inconsistências, calcula estatísticas, visualiza os dados e responde a perguntas relacionadas às vendas.
- **Links para o Google Colab**: O arquivo original foi carregado no Google Colab, e o link para acessá-lo é fornecido.

## Funcionalidades

### 1. Leitura e Manipulação de Dados
- O código começa importando os dados diretamente de uma planilha do Google Sheets.
- O tipo de dados das colunas é ajustado para garantir a precisão da análise (como conversão da coluna `Date` para datetime).
- O código verifica e trata valores nulos e duplicados, garantindo a integridade dos dados.

### 2. Estatísticas Descritivas
- O código calcula a média, moda, e mediana de variáveis como `Price`, `Discount`, e `Quantity`.
- O intervalo interquartílico (IQR) é utilizado para detectar possíveis outliers nos dados.

### 3. Análise de Correlação
- É gerada uma matriz de correlação entre as variáveis numéricas.
- Um gráfico de mapa de calor é gerado para visualizar essas correlações.

### 4. Visualização dos Dados
Diversos gráficos são gerados para entender o comportamento das vendas, incluindo:
- **Produtos Mais Vendidos por Categoria**: Um gráfico de barras para mostrar os produtos mais vendidos dentro de cada categoria.
- **Vendas por Região**: Um gráfico de mapa de calor que mostra em quais regiões as vendas foram mais expressivas.
- **Relação entre Descontos e Aumento de Vendas**: Um gráfico de barras para verificar a relação entre a quantidade de vendas e os descontos aplicados.
- **Volume de Vendas por Dia da Semana**: Um gráfico de barras para mostrar os dias da semana com maior volume de vendas.
- **Faturamento por Dia da Semana**: Um gráfico de linha para analisar o faturamento em cada dia da semana.

### 5. Perguntas Respondidas
O código responde às seguintes perguntas:
1. Quais são os produtos mais vendidos por categoria?
2. Em quais regiões as vendas foram mais expressivas?
3. Existe relação entre os descontos e o aumento de vendas?
4. Quais dias da semana possuem maior volume de vendas?
5. Qual dia da semana tem o maior faturamento?

## Tecnologias Utilizadas

- **Pandas**: Manipulação e análise de dados.
- **Matplotlib e Seaborn**: Visualização de dados.
- **Google Colab**: Ambiente de desenvolvimento para execução do código.
- **Numpy**: Operações matemáticas e manipulação de arrays.
- **Datetime**: Manipulação de datas e horários.

## Como Executar

Para executar o código localmente, siga os passos abaixo:

1. **Instale as dependências**:
   Certifique-se de ter o Python 3 instalado, juntamente com as bibliotecas necessárias. Você pode instalar as bibliotecas necessárias utilizando o seguinte comando:

pip install pandas matplotlib seaborn numpy


2. **Execute o código**:
O código pode ser executado em qualquer ambiente de desenvolvimento que suporte Python, como Jupyter Notebook, VSCode, ou diretamente no Google Colab.

Se você deseja executar o código diretamente no Google Colab, acesse: https://colab.research.google.com/drive/1Qffk_p3MIRnaodfgeWAZkHj_RGp8KSLA?usp=sharing

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou ajustes. Se você encontrar algum bug ou tiver sugestões, abra uma *issue* ou envie um *pull request*.

