import os
os.system('cls')

def verifica_lista_inteiro(list: list) -> bool:
    inteiros = True
    for i in range (0, len(list), 1):
        list[i] = str(list[i])
        if not list[i].isnumeric():
            return False
    return inteiros


# ----------- programa principal para testar a função
lista = [5,8,4,"Edson", 12, 44]
if verifica_lista_inteiro(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print("Nem todos os elementos contidos no laço são inteiros")

lista2 = [5,8,4,12,44]
if verifica_lista_inteiro(lista2):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print("Nem todos os elementos contidos no laço são inteiros")

print(lista)
print(lista2)