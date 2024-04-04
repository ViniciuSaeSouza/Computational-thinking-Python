import os
os.system('cls')

n = int(input("Numero: "))

mult = 1

while mult <= 10:
    tab = n * mult
    print(tab, end="\n")
    mult += 1