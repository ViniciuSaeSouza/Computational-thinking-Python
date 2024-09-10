import os
import json

os.system('cls')

# JSON  = JavaScript Object Notation

# Criando um dicionário aninhado
pessoas = {
  'pessoa1': {
    'nome' : 'Edson',
    'idade' : 50,
    'email' : 'eds@fiap.com.br'
  },
  'pessoa2': {
    'nome' : 'Maria',
    'idade' : 18,
    'email' : 'maried@fiap.com.br'
  },
  'pessoa3': {
    'nome' : 'Laura',
    'idade' : 18,
    'email' : 'laurinha@fiap.com.br'
  }
}

# <obj_gravado_arq> = json.dumps(<dict>)
pessoas_json = json.dumps(pessoas, indent=2)
# print(pessoas)
# print(pessoas_json)


# Gravando no arquivo json com o '.write'
with open("arquivo.json" , 'w+', encoding='utf8') as file:
  file.write(pessoas_json)
  
with open('arquivo.json', 'r') as file:
  pessoas_json = file.read()
  pessoas = json.dumps(pessoas_json)
  
  print(pessoas_json)
  print(pessoas)

  