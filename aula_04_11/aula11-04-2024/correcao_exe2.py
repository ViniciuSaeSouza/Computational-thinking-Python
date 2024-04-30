'''
2. Peça dois numeros ao usuário e os exiba em ordem crescente se o primeiros for
menor que o segundo ou em ordem decrescente se o primeiro numero for maior que o
segundo. 
Entrada 1: 5  8     Saída 1: 5 6 7 8
Entrada 2: 8  5     Saída 2: 8 7 6 5
'''
import os
os.system("cls")
num1 = int(input('Inicio: '))
num2 = int(input('Fim: '))

if num1 <= num2:
    for i in range(num1, num2 + 1, 1):
        print(i, end = ' ')
else:
    for i in range(num1, num2 -1, -1):
        print(i, end = ' ')






