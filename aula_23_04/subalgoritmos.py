import math
import os

#=============== SUBALGORITMOS
# --- PROCEDIMENTO: Rotina que não retorna valor ao código chamador
# def <nome_subalgoritmo> (<parâmetros>):
#       <corpo do procedimento>
def saudacao1() -> None:
    print("Bom dia, Usuário!")

def saudacao2(nome: str) -> None:
    print(f'Bom dia {nome}')
    
def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        msg = 'Bom dia'
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {nome}!")

# --- Função: Rotina que retorna um valor ao código chamador
# def <nome_subalgoritmo> (<parâmetros>):
#     <corpo do da funcao>
#     return <valor a ser retornado>
def pi() -> float:
    return 3.1415

def soma3 (n1: float, n2: float, n3: float) -> float:
    s = n1 + n2 + n3
    return s


def calcula_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media
#================== PROGRAMA PRINCIPAL

os.system('cls')
saudacao1()
saudacao2("Saes")
n = input("Nome: ")
saudacao2(n)

saudacao3("Saes", 12)

print(pi())

print(soma3(1,4,5))


print(calcula_media(10,9,8))
