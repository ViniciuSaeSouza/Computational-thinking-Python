import os
import funcoes_menu
"""
Crie um dicionario no formato:
notas = {
    "Edson": 10, - chave: nota do aluno, cabivel estar em maiusculo
    "Maria": 5, - dado float
}

e faça as seguintes funcionalidades:

1 - SAIR
2 - Adicionar novo aluno | Nota (limite de 10 alunos) - usar o for
3 - Editar Aluno | Nota - duas entradas, se o aluno existe eu edito
4 - Excluir um aluno
5 - Calcular a média da turma - método value
6 - Apagar todos os alunos
7 - Consultar um aluno
8 - Listar as notas e os nomes

"""

"""
Nome: Marcelo  - verificar se o nome já existe - gets
Nota: 9
Gravado

cenario2:
Nome: Edson - não gravar o mesmo nome
aparecer um já existe - get

* >= 10 alunos

Cenário 3:
Nome: Maria
Nota: 6
mensagem: gravou

se existir eu passo
se não existir eu gravo

upper - pra deixar maiusculo ou minusculo

nota invalida, voltar pro menu - o nome não ta gravado tbm

"""

# Dicionário de nomes (key) e notas(value)
notas = {
  "Edson": 10, 
  "Maria": 5
}


def listar_nomes_e_notas():
  for nome, nota in notas.items():
    print(f"Nome: {nome} --> Nota: {nota}")


# Mostra o título da página em maíusculo e com linha de asteriscos em baixo com o tamanho do título.
def mostra_titulo(titulo:str) -> None:
  print(titulo.upper())
  print("*" * len(titulo))

# Lista todas as opções do menu

def adicionar_novo_aluno():
  #teste
  print()
def editar_aluno():
  #teste
  print()
def excluir_aluno():
  #teste
  print()
def calcular_media_da_turma():
  #teste
  print()
def apagar_todos_os_alunos():
  #teste
  print()
def consultar_aluno():
  #teste
  print()
def sair():
  #teste
  print()

opcoes = {
  "1" : listar_nomes_e_notas,
  "2" : adicionar_novo_aluno,
  "3" : editar_aluno,
  "4" : excluir_aluno,
  "5" : calcular_media_da_turma,
  "6" : apagar_todos_os_alunos,
  "7" : consultar_aluno,
  "8" : sair
}
     
def lista_menu():
  for k, v in opcoes.items():
    value_formatado = str(v).replace('_'," ").capitalize()
    print(f"{k} - {value_formatado}")

def menu():
  os.system('cls')
  while True:
    mostra_titulo("menu")
    lista_menu()
    escolha = input("Escolha: ")
    if escolha not in opcoes:
      print(f"ERRO! Escolha '{escolha}' inválida (fora do range de 1 até 8).")
      input("Digite qualquer tecla para voltar ao menu: ")
    else:
      opcoes[escolha]()
      
menu()