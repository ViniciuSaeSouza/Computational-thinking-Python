# exercicio 02
import json

with open("funcionarios.txt", "r", encoding="utf-8") as file:
    funcionarios = file.readlines()

ti = []
for funcionario in funcionarios:
    if 'TI' in funcionario:
      ti.append(funcionario)

with open("ti.txt", "w",encoding="utf-8") as file:
    file.writelines(ti)

funcionarios_ti = {}

for i, elemento in enumerate(ti):
 id, nome, cargo = elemento.split(",")
 funcionarios_ti[f'funcionario{i+1}'] = {'id' : id, 'nome' : nome, 'cargo' : cargo.strip()}

with open("funcionarios_ti.json", "w+", encoding= "utf-8") as file:
    json.dump(funcionarios_ti, file, indent=4,  ensure_ascii=False)
    file.seek(0)
    print(file.read())