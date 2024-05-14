import os
os.system("cls")
#        012345678901234567890123456789012345678901
frase = "Dia 29 é aniversário de alguem, quem será?"

# Método find: retorna o índice do valor procurado, caso contrário retorna o valor -1
"""print(frase.find("de"))
print(frase.find("9"))
print(frase.find("moio"))

if frase.find("moio") == -1:
    print("Este trecho não existe")
else:
    print("encontrou")

#Exercício: retornar todos os indices de uma substring procurada
#a ===> 2 9 24"""


# O método join transforma uma lista de strings em uma string
"""lista_str = ["Edson", "de", "Oliveira"]
print(lista_str)
print(" ".join(lista_str))

nome = "-".join(lista_str)
print(nome)"""

# O método split é o contrário do jon, ou seja, pega uma string e transforma numa lista de string

nome = "Vinicius Saes de Souza"
print(nome)
lista_str = nome.split()
print(lista_str)

lista_str = nome.split("e")
print(lista_str)

lista_str = nome.split("ni")
print(lista_str)


