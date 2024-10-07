# ax² + bx + c
# a = 1 / b = -5 / c = 6

# RM 554456 - VINÍCIUS SAES DE SOUZA
import os
import math
from typing import Tuple

def verifica_igual_zero(numero: float) -> bool:
    if numero == 0:
        return True
    else:
        return False

def calcula_delta(a: float, b: float, c: float) -> float:
    delta = (math.pow(b, 2)) - 4 * a * c
    return delta


def bhaskara(a: float, b: float, delta: float) -> tuple[float, float]:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2

def converte_float(item:str) -> float:
    try:
        numero = float(item)
        return numero
    except:
        print("Favor digitar um número!")
        input("Aperte qualquer tecla para recomeçar.")
        menu()

def verifica_equacao_incompleta(num1: float, num2: float) -> bool:
    if verifica_igual_zero(num1) or verifica_igual_zero(num2):
        return True
    else:
        return False

def verifica_negativo(item:float) -> bool:
    if item < 0:
        return True
    else:
        return False

def verifica_continuar(inpt: str) -> str:
    opcoes = ["S", "N"]
    if inpt.upper() in opcoes:
        return inpt.upper()
    else:
        return "F"


def continuar_sistema():
    continuar = verifica_continuar(input("Continuar executando o programa? [S]im ou [N]ão: "))
    match continuar:
        case "S":
            menu()
        case "N":
            print("Finalizando....")
            exit()
        case _:
            print("Digite uma opção válida!")
            continuar_sistema()


def menu():
    os.system('cls')
    while(True):
        print(" -- EQUAÇÕES SEGUNDO GRAU -- ")
        print("Digite as varáveis para calcular:")
        a = converte_float(input("A: "))

        if verifica_igual_zero(a):
            print("Esta equação não é do segundo grau, sim do primeiro.")
            break

        b = converte_float(input("B: "))
        c = converte_float(input("C: "))


        delta = calcula_delta(a, b, c)
        
        if verifica_negativo(delta):
            print(f"Delta 🔺: {delta}")
            print("Não é possível calcular x1 e x2 porque o delta é negativo")
            break
        else:
            x1, x2 = bhaskara(a, b, delta)
        
        if verifica_igual_zero(delta):
            print(f"Delta 🔺: {delta}")
            print(f"X1: {x1} \nX2: {x2}")
            print("As raízes x1 e x2 tem o mesmo valor")
            break

        elif verifica_equacao_incompleta(b, c):
            print(f"Delta 🔺: {delta}")
            print(f"X1: {x1} \nX2: {x2}")
            print("Equação do segundo grau INCOMPLETA")
            break
        else:
            print(f"Delta 🔺: {delta}")
            print(f"X1: {x1} \nX2: {x2}")
            print("Equação do segundo grau COMPLETA\n As raízes x1 e x2 tem valores distintos")
            break

    continuar_sistema()


menu()
