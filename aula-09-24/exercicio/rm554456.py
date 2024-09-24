# RM 554456 - Vinícius Saes de Souza

import json

# with open("dados.txt", "w", encoding="utf-8") as arquivo:
#   arquivo.write("""12345t, edson@fiap.com.br
# 01020d, maria@hotmail.com
# 1abcde, estela@ig.com.br
# 123abd, vania@terra.com.br""")


with open ('dados.txt', 'r', encoding='utf-8') as arquivo:
  arquivo.seek(0)
  dados = arquivo.readlines()
  # dados_lidos = json.loads(dados)
  print(dados)