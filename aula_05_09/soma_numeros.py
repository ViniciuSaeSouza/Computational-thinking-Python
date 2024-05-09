def soma_numeros(*args: list) -> float: #utiliza 'args' quando não sabe o número de parametros a serem passados
    soma = 0
    for i in range(0, len(args), 1):
        soma = soma + args[i]
    return soma

import os
os.system('cls')

print(f"Soma dos números: {soma_numeros(-5, -9)}")