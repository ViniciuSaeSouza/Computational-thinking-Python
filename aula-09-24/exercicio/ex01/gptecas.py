# exercicio 01
import json

with open("produtos.txt", "r") as file:
    dados = file.readlines()
    aux = []
    ids = []
    precos = []
    for elemento in dados:
        aux.append(elemento.split(","))

    for i in range(0, len(aux), 1):
        ids.append(aux[i][0].strip() + "\n")
        precos.append(aux[i][2].strip() + "\n")

with open("ids.txt", "w") as file:
    file.writelines(ids)

with open("precos.txt", "w") as file:
    file.writelines(precos)

print("ID'S:")
ids_txt = open("ids.txt", "r")
print(ids_txt.read())

print("Preços: ")
precos_txt = open("precos.txt", "r")
print(precos_txt.read())

produtos = {}

for i in range(0, len(ids),1):
    produtos[f"produto{i+1}"] = {'id' : ids[i].strip(), 'preco' : precos[i].strip()}

with open("produtos.json", "w") as file:
    json.dump(produtos, file, indent = 4)

ids_txt.close()
precos_txt.close()