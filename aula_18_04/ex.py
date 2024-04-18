v = [45, -89, 32, -12, 33]

import os
os.system('cls')

# print(v)

# for i in range(0, 5, 1):
#     numero = input("Digite os números: ")
#     numero = int(numero)
#     v[i] = numero
#     # print(f"Elemento[{i}]= {v[i]:6.2f}" )
# print(v)

# print(v[0])

# for i in range (0, 5, 1):
#     if v[i] < 0:
#         print(v[i], end=" ")

# 3 / 4 -
soma = 0
for i in range(0,5,1):
    soma += v[i]   
media = soma / 5 
print("Soma: ", soma)
print("Media: ", media)
# for i in range(0, 5, 1):
#     media = soma / 5

# 5- 
for i in range(0,5,1):
    if v[i] % 2 != 0:
        print(f"V[{i}]= {v[i]}")
