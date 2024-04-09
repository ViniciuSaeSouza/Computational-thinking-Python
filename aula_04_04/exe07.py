"""
3. Peça dois numeros ao usuário e a ordem ("C"rescente ou "D"ecrescente) e exiba
o intervalo devido.
Entrada 1: 5  8  D   Saída 1: 8 7 6 5
Entrada 2: 8  5  C   Saída 2: 5 6 7 8
"""
import os
os.system('cls')

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
mod = inicio
ordem = str(input(
"""
C - Ordem crescente
D - Ordem decrescente
Escolha: """
))
ordemMaiusculo = ordem.capitalize()

# Laço for
if ordemMaiusculo == "C":
    if inicio > fim:
        aux = inicio
        inicio = fim
        fim = aux
    for i in range(inicio, fim + 1, 1):
        print(i)
elif ordemMaiusculo == "D":
    if inicio < fim:
        aux = inicio
        inicio = fim
        fim = aux
    for i in range(inicio, fim - 1, -1):
        print(i)
else:
    print("Digite uma opção válida!")
    


# Laço while
# if ordemMaiusculo != "C" or ordemMaiusculo != "D":
#         print("Escolha uma opção válida")

# if ordemMaiusculo == "C" and inicio < fim:
#         print("Ordem Crescente: ")
#         while inicio <= fim:
#                 print(inicio)
#                 inicio += 1
# elif ordemMaiusculo == "C" and inicio > fim:
#         while inicio >= fim:
#                 print(fim)
#                 fim += 1
# elif ordemMaiusculo == "D" and inicio < fim:
#         print("Ordem Decrescente: ")
#         while inicio <= fim:
#                 print(fim)
#                 fim -= 1
# else:
#         while inicio >= fim:
#                 print(inicio)
#                 inicio -= 1