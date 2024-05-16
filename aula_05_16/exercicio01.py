import os
os.system('cls')

"""def vogal_maiuscula(nome:str) -> str:
    vogal = 'aeiou'
    for i in range(len(nome)):
        if nome[i] in vogal:
            nome = nome.replace(nome[i], nome[i].upper())

    return nome"""


def vogal_maiuscula(nome:str) -> str:
    vogal = 'aeiou'
    for i, carac in enumerate(nome):
        if carac in vogal:
            nome = nome.replace(carac, carac.upper())
    return nome


texto = "Vinicius Saes de Souza"
new_texto = vogal_maiuscula(texto)
print(new_texto)