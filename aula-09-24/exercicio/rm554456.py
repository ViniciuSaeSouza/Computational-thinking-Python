# RM 554456 - Vinícius Saes de Souza

import json
# Definição de caminhos para os arquivos a serem criados/lidos
caminho_arquivo_dados = "dados.txt"
caminho_arquivo_login = "login.txt"
caminho_arquivo_email = "email.txt"
caminho_arquivo_json = "login_senha.json"

# Teste para ver como seria para criar os arquivos na pasta atual do arquivo .py
"""
import os
caminho_atual = os.path.dirname(__file__)
caminho_arquivo_dados = os.path.join(caminho_atual, "dados.txt")
caminho_arquivo_login = os.path.join(caminho_atual, "login.txt")
caminho_arquivo_email = os.path.join(caminho_atual, "email.txt")
caminho_arquivo_json = os.path.join(caminho_atual, "login_senha.json")
"""

# Criação do arquivo de dados com informações de login e email
with open(caminho_arquivo_dados, "w", encoding="utf-8") as arquivo:
  arquivo.write("""12345t, edson@fiap.com.br
01020d, maria@hotmail.com
1abcde, estela@ig.com.br
123abd, vania@terra.com.br""")

# Funções auxiliares para processamento de dados

# Remove quebras de linha de uma lista de strings
def remove_quebra_linha(lista: list[str]) -> list[str]:
  aux = []
  for string in lista:
    aux.append(string.removesuffix("\n"))
  return aux

# Cria arquivo de login a partir de dados lidos
def cria_arquivo_login(dados_lidos: list[str]) -> list[str]:
  lista_aux = []
  with open(caminho_arquivo_login, "w", encoding="utf-8") as arquivo:
    for string in dados_lidos:
      string_aux = string.split(',')
      login = string_aux[0] + "\n"
      lista_aux.append(login)
    arquivo.writelines(lista_aux)
  return lista_aux

# Cria arquivo de email a partir de dados lidos
def cria_arquivo_email(dados_lidos: list[str]) -> list[str]:
  lista_aux = []
  with open(caminho_arquivo_email, "w", encoding="utf-8") as arquivo:
    for string in dados_lidos:
      string_aux = string.split(',')
      email = string_aux[1].strip() + "\n"
      lista_aux.append(email)
    arquivo.writelines(lista_aux)
  return lista_aux

# Cria arquivo JSON a partir de listas de logins e emails
def cria_arquivo_json(lista_logins: list[str], lista_emails: list[str]):
  dict_aux = {}
  with open(caminho_arquivo_json, "w", encoding="utf-8") as arquivo:
    for i in range(0, len(lista_logins), 1):
      dict_aux[lista_logins[i]] = {'email': lista_emails[i]}
    json.dump(dict_aux, arquivo, indent=2)

# Mostra logins armazenados no arquivo de login
def mostra_logins(lista_logins: list[str]) -> None:
  print("login.txt")
  for login in remove_quebra_linha(lista_logins):
    print(login)

# Mostra emails armazenados no arquivo de email
def mostra_emails(lista_emails: list[str]) -> None:
  print("\nemail.txt")
  for email in remove_quebra_linha(lista_emails):
    print(email)

# Exibe conteúdo do arquivo JSON
def exibe_arquivo_json():
  with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo:
    json_lido = json.load(arquivo)
    print("\nlogin_senha.json")
    print(json_lido)

# Leitura do arquivo de dados e processamento
with open(caminho_arquivo_dados, "r", encoding="utf-8") as arquivo:
  arquivo.seek(0)
  dados_lidos = remove_quebra_linha(arquivo.readlines())
  
  # Cria arquivos de login e email
  lista_logins = cria_arquivo_login(dados_lidos)
  lista_emails = cria_arquivo_email(dados_lidos)
  
  # Mostra conteúdo dos arquivos de login e email
  mostra_logins(lista_logins)
  mostra_emails(lista_emails)
  
  # Cria arquivo JSON
  cria_arquivo_json(remove_quebra_linha(lista_logins), remove_quebra_linha(lista_emails))
  
  # Exibe conteúdo do arquivo JSON
  exibe_arquivo_json()