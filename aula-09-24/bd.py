import os
import oracledb
import pandas as pdiddy

try:
  conn = oracledb.connect(user="RM554456", password="080995", dsn="oracle.fiap.com.br:1521/ORCL")
  # Criar os cursores
  insert_cadastro = conn.cursor("INSERT INTO ")
except Exception as e:
  print("Conexão deu erro" , e)
  conexao = False
else:
  print("Conexão aberta com sucesso!")
  conexao = True
  
while conexao:
  os.system('cls')
  print("""
MENU
---
0 - SAIR
1 - Cadastrar PET        
""")
  escolha = int(input("Escolha: "))
  match escolha:
    case 0:
      break
    case 1:
      try:
        tipo = input("Tipo do pet: ")
        nome = input("Nome do pet: ")
        idade = int(input("Idade do pet: "))
        cadastro = f"INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES ('{tipo}', '{nome}', {idade})"
        insert_cadastro.execute(cadastro)
        conn.commit()
      except ValueError:
        print("Deu ruim")