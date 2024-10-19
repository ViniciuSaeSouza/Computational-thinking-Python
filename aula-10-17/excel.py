import os

import pandas as pd

os.system('cls' if os.name == 'nt' else 'clear')

dados = {
    'nome' : ['Edson', 'Maria', 'Ester'],
    'idade' : [25, 44, 65],
    'cidade' : ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'tamanhoDoPiru' : ['17cm', '27cm', '15cm']
}


# Converte o dicionário em um DataFrame
df = pd.DataFrame(dados)

# Salva o Dataframe em um arquivo Excel
nome_arquivo = 'planilha.xlsx'

df.to_excel(nome_arquivo, index=False)
print(f"o arquivo {nome_arquivo} foi criado")

teste = pd.read_excel('planilha.xlsx')

print(teste)

