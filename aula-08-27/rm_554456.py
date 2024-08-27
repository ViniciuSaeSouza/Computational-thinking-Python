#Vinicius Saes de Souza - RM554456
import os
nome_lista = [] #Lista que amarzena cada elemento do Nome Completo

# Função que espera qualquer input e aciona o menu()
def volta_menu():
  input("Digite qualquer tecla para voltar ao menu: ")
  menu()

# Função que verifica se há um nome na lista, se estiver vazia retorna `False`, se não, retorna `True`
def verifica_nome_lista() -> bool:
  if not nome_lista:
    print("ERRO! Primeiramente digite um nome na opção 1")
    return False
  else:
    return True

# Captura input do nome completo e extende a lista de cada elemento do nome á lista `nome_lista`
def grava_nome_completo() -> None:
  os.system('cls')
  nome_completo = input("Digite um nome completo: ")
  while (not nome_completo):
    print("\nERRO! Nome não pode ser vazio.")
    nome_completo = input("Digite um nome completo: ")
  nome_lista.extend(nome_completo.split(" ")) 
  volta_menu()

# Se houver nome na lista, 
def exibe_nome_separado() -> None:
  if not verifica_nome_lista():
    print("ERRO! Primeiramente digite um nome na opção 1")
  else:
    sobrenome = " ".join(nome_lista[1:])
    print(f"Nome: {nome_lista[0]}")
    print(f"Sobrenome: {sobrenome}")
    
  volta_menu()

def numero_palavras_nome() -> None:
  if not verifica_nome_lista():
    print("ERRO! Primeiramente digite um nome na opção 1")
  else:
    nome_completo = " ".join(nome_lista)
    print(f"O nome {nome_completo} tem {len(nome_lista)} palavras")
  volta_menu()
  
def exibe_bibliografia() -> None:
  if not verifica_nome_lista():
    print("ERRO! Primeiramente digite um nome na opção 1")
  else:
    nome = " ".join(nome_lista[0:-1])
    sobrenome = " ".join(nome_lista[-1:])
    print(f"{sobrenome.upper()}, {nome}")
  volta_menu()


def menu():
  os.system('cls')
  print("""
  --MENU--
  
0 - SAIR
1 - Digitar nome completo
2 - Exibe o nome separado do sobrenome
3 - Conta quantas palavras há no nome completo
4 - Exibe nome em formato de bibliografia
""")
  while(True):
    escolha_menu = input("Escolha: ")
    try:
      escolha_menu = int(escolha_menu)
    except ValueError:
      print(f"ERRO! Escolha inválida")
      volta_menu()
      
    match escolha_menu:
        case 0:
          exit()
        case 1:
          grava_nome_completo()
        case 2:
          exibe_nome_separado()
        case 3:
          numero_palavras_nome()
        case 4:
          exibe_bibliografia()
        case _:
          "ERRO! Escolha inválida."

menu()