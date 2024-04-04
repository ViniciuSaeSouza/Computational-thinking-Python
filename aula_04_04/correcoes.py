import os
os.system('cls')

#Pedir dois numeros ao usuario, exibir o intervalo sem considerá-los

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

inicio += 1

while inicio < fim:
    print(inicio)
    inicio += 1


