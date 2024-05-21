import os
os.system('cls')


def isinteiro(s: str) ->bool:
    digito = '0123456789'
    valido = True
    if s[0] in '+-' or s[0] in digito:
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False
#    01234
x = '-3456'

# ------------ Programa principal

while True:
    x = input('Digite um inteiro: ')
    if not isinteiro(x):
        x = input("Erro\nDigite um inteiro: ")
    else:
        x = int(x)
        break


# print(isinteiro('j1234'))
# print(isinteiro('99'))
# print(isinteiro('-45'))
# print(isinteiro('+44.'))
# print(isinteiro('+232'))