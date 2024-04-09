#2. Peça dois numeros ao usuário e os exiba em ordem crescente se o primeiro for menor que o segundo ou em ordem decrescente se o primeiro numero for maior que o segundo.
#Entrada 1: 5 8 Saída 1: 5 6 7 8
#Entrada 2: 8 5 Saída 2: 8 7 6 5

import os
os.system('cls')
print("Exercicio .2")
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o final: "))

# Laço for

if inicio > fim:
    for i in range(inicio, fim - 1, -1):
        print(i)
else:
    for i in range(inicio, fim +1, 1):
        print(i)

#  Laço while
if inicio < fim:
    num = inicio
    while num <= fim:
        print(num)
        num += 1
else:
    num = inicio
    while num >= fim:
        print(num)
        num -= 1