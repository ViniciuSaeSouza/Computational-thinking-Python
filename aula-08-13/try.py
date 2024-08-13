# Tratamento de erros

"""
try:
    comandos a serem executados
except:
    mensagem ou tratamento do erro
else:
    entrará neste ponto caso não haja erro
finally:
    executará independentemente de ter erro ou não
"""

import os
os.system("clear")




try:
    print("Calculando a divisao de 2 numeros: ")
    valor1 = float(input("valor 1: "))
    valor2 = float(input("valor 2: "))
    divisao = valor1 / valor2
    print(f"Divisão = {divisao}")
except ValueError: # Trabalhando o erro pela constante
    print("Digite um valor numérico")
except ZeroDivisionError as erroDivisaoPorZero: # Trabalhando o erro pela descrição
    print(erroDivisaoPorZero)
except:
    print("Cara! Chame o administrador porque ferrou tudo")
else:
    print("Divisão efetuada com sucesso!")
finally:
    print("Obrigado por utilizar o nosso sistema")





"""
n = input("Nota: ")
if n.isnumeric():
    n = int(n)
    print(n)
else:
    print("Erro, nao é numero")
"""