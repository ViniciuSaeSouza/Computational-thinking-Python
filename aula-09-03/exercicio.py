"""
Exercício:
Crie o seguinte menu:
 
0 - SAIR
1 - Gravar o arquivo
2 - Ler o arquivo
3 - Editar o arquivo
"""

def gravar_arquivo():
  nome_arquivo = input("Digite o nome do arquivo txt: ")
  info = input("Digite o que vai ser gravado no arquivo: ")
  arquivo = open(nome_arquivo, 'w', encoding='utf-8')
  try:
    arquivo.write(info)
    arquivo.close()
  except FileNotFoundError:
    print("ERRO! Arquivo não encontrado")  
  menu()
  
def ler_arquivo():
  escolhe_arquivo = input("Arquivo para ser lido: ")
  try:
    arquivo = open(escolhe_arquivo, 'r', encoding='utf-8')
    print(arquivo.read())
    arquivo.close()
  except FileNotFoundError:
    print("ERRO! Arquivo não existe.")
  menu()
  
def editar_arquivo():
  escolhe_arquivo = input("Arquivo para ser editado: ")
  try:  
    arquivo = open(escolhe_arquivo, 'a', encoding='utf-8')
    edicao = input("Informação: ")
    arquivo.write(f"\n{edicao}")
    arquivo.close()
  except FileNotFoundError:
    print("ERRO! Arquivo não encontrado")
  menu()

def menu():
  print("""
0 - Sair
1 - Gravar o arquivo
2 - Ler o arquivo
3 - Editar o arquivo        
""")
  escolha = input("Escolha: ")
  match escolha:
    case "0":
      exit()
    case "1":
      gravar_arquivo()
    case "2":
      ler_arquivo()
    case "3":
      editar_arquivo()
      
menu()