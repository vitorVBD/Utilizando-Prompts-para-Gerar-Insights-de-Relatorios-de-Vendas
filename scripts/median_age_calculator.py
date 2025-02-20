import pandas as pd

# Carregar a planilha CSV
df = pd.read_csv('caminho/para/sua/planilha.csv')

# Calcular a média de idade dos compradores de cada produto e em cada país
media_idade = df.groupby(['Produto', 'País'])['Idade'].mean().reset_index()

# Exibir o resultado
print(media_idade)