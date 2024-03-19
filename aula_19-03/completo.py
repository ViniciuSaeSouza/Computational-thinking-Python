import os
os.system('cls')

# Nota Inválida
nota = float(input("Nota: "))

if nota >=0 and nota <=10:
    print("Nota válida!")
else:
    print("Nota")

#Calcula a media e vê se está aprovado ou reprovado
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
#nota3 = float(input("Nota 3: "))

media = (nota1 + nota2) / 2

if media > 6:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("Exame")
    
#Calcular a media das duas maiores notas
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

menor = nota1

if nota2 < menor:
    menor = nota2

if nota3 < menor:
    menor = nota2

media = (nota1 + nota2 + nota3 - menor) / 2

"""
CENÁRIO 1:
nota1: 45
Nota inválida!

Cenário 2:
nota1: 5
nota 2: -5
Nota inválida!

CENÁRIO 3:
nota 1: 5
nota 2: 4
nota 3: 423
Nota inválida!

CENÁRIO 4:
Nota 1: 0
Nota 2: 8
Nota 3: 9
Aprovado média 8.5 | Exame | Reprovado
"""