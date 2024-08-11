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
import os
os.system("cls")

notas = {
    "Edson": 10, 
    "Maria": 5,
}

def exibir_menu():
    print("\nMENU: ")
    print("\n1 - SAIR")
    print("\n2 - Adicionar novo aluno | Nota (limite de 10 alunos)")
    print("\n3 - Editar Aluno | Nota")
    print("\n4 - Excluir um aluno")
    print("\n5 - Calcular a média da turma")
    print("\n6 - Apagar todos os alunos")
    print("\n7 - Consultar um aluno")
    print("\n8 - Listar as notas e os nomes")


# def sair():

def adicionar_aluno_novo(notas):
    if len(notas) >= 10:
        print("Limite de 10 alunos atingido")
        return
    
    nome_aluno = input("Nome: ").upper()
    if nome_aluno in notas:
        print("Nome já existente")
        return
    nota = input("Nota: ")
    if nota.replace('.', '', 1).isdigit() and nota.count('.') < 2: # validando
        nota = float(nota)
        if 0 <= nota <= 10:
            notas[nome_aluno] = nota
            print("Gravado !")
        else:
            print("Colocar uma nota válida")    
    else:
        print("Nota inválida! Por favor, insira um número entre 0 e 10")        

def editar_aluno_ou_nota(notas):
    nome = input("Nomo do aluno que deseja editar: ").upper()
    if nome not in notas:
        print("Aluno não encontrado.")




exibir_menu()    

    
