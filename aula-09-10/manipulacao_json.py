import os
import json

os.system('cls')

#criando um dicionário

contato = {
  'nome' : 'Edson',
  'idade' : 50,
  'cel' : '1194739543'
}

# gravando o dicionario em um arquivo json

with open("cadastro.json", 'w', encoding='utf8') as arquivo:
  # json.dump(<dict>, <file_object>)
  json.dump(contato, arquivo)
  
# Ler e imprimir na tela o arquivo .json
with open("cadastro.json", 'r', encoding="utf8") as arq:
  # <dict> = json.load(<file_obj>)
  dados_lidos = json.load(arq)
  print(dados_lidos)
  
# Modificar os dados do arquivo json
with open("cadastro.json", 'r', encoding='utf8') as arq:
  dados_modificados = json.load(arq)
  # modificando os dados
  dados_modificados['idade'] = 48
  dados_modificados['cel'] = '12948372564'
  
# Gravando dicionário no arquivo
with open("cadastro.json", "w", encoding='utf8') as arq:
  json.dump(dados_modificados, arq)
  print(dados_modificados)


