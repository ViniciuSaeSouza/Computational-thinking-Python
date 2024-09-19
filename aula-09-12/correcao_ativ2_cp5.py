# Subalgoritmos ---------
def cadastrar_registro(id: str, registros: dict) -> None:
    nome = input("Nome: ")
    idade = input("Idade: ")
    registros[id] = {'cpf' : id,'nome': nome, 'idade' : idade}

def exibe_registro(registro: str) -> None:
    print(f"""
    CPF: {registro['cpf']}
    NOME: {registro['nome']}
    IDADE: {registro['idade']}""")
        

def editar_registro(id: str, registro: dict) -> None:
    exibe_registro(registro[id])
    nome = input("Novo nome: ")
    idade = input("Nova idade: ")
    if nome != '':
        registro[id]['nome'] = nome
    if idade != '':
        registro[id]['idade'] = idade
    

#------------------
import os
os.system('cls')
pessoas = {}

continua  = True

while continua:
    cpf = input("CPF: ")
    if cpf == "":
        continua = False
    elif cpf in pessoas:
        #editar....
        editar_registro(cpf, pessoas)
    else:
        cadastrar_registro(cpf, pessoas)
else:
    print("Programa finalizado")
