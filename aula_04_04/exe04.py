# dado 10 números, exibir o de maior valor

volta = 1 

print("Digite 10 numeros: ")

maior = 0 

while volta <= 10:
    num = int(input())
    if num > maior:
        maior = num
    volta += 1

print(f"Maior = {maior}")