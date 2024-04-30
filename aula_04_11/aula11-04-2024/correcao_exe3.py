''' 
3. Peça dois numeros ao usuário e a ordem ("C"rescente ou "D"ecrescente) e exiba
o intervalo devido.
Entrada 1: 5  8  D   Saída 1: 8 7 6 5
Entrada 2: 8  5  C   Saída 2: 5 6 7 8
'''

import os
os.system("cls")
num1 = int(input('Inicio.......................: '))
num2 = int(input('Fim..........................: '))
ordem = input("[C]rescente ou [D]ecrescente? ")

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

if ordem == 'c' or ordem == 'C':
    for i in range(menor, maior + 1, 1):
        print(i, end = ' ')
elif ordem.upper() == "D":
    for i in range(maior, menor - 1, -1):
        print(i, end = ' ')
else:
    print("Digite C ou D")

