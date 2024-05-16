# Dada uma lista e um caracter por parâmetro, faça uma função que retorne em uma lista com os índices onde os caracteres foram encontrados.
import os
os.system('cls')

def retorna_indices(nome:str, letra:str) -> list:
    lista_indices = list()
    for i in range(len(nome)):
        if nome[i] == letra:
            lista_indices.append(i)
    return lista_indices

nome = "Edson de Oliveira"

print(retorna_indices(nome, 'e'))

print(retorna_indices(nome,'a'))

print(retorna_indices(nome,'m'))