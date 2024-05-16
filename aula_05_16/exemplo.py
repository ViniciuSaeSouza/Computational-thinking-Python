# Dada uma lista com notas, faça uma função que retorne outra lista comente com as notas maiores ou igual a 6.

# -------------------- Programa principal

import os
os.system('cls')

def verifica_aprovados (l: list) -> list:
    nova_lista = list()
    for i in range(len(l)):
        if l[i] >= 6:
            # lista_aprovados.append(i)
            nova_lista.append(l[i])
    return nova_lista


lista_notas = [10, 5, 6, 7.5, 9, 3, 0]

lista_aprovados = verifica_aprovados(lista_notas)

print(lista_aprovados)

# >>[10, 6, 7.5 , 9]