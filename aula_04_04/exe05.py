# 1. Peça dois numeros ao usuario e os exiba em ordem crescente. Se o primeiro for maior do que o segundo numero, exibir o intervalo da mesma forma
# Entrada 1: 5 8 Saída 1: 5 6 7 8
# Entrada 2: 8 5 Saída 2: 5 6 7 8

import os
os.system('cls')

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o final: "))

# Laço for

if inicio > fim:
    auxiliar = inicio
    inicio = fim
    fim = auxiliar

for i in range(inicio, fim + 1, 1):
    print(i)

# # Laço while
# if inicio <= fim:
#     num = inicio
#     while num <= fim:
#         print(num)
#         num += 1
# else:
#     num = fim
#     while num <= inicio:
#         print(num)
#         num += 1








