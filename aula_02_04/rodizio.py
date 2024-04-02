import os
os.system ('cls')


placa = input("Digite os digitos da sua placa: ")


if placa.isnumeric():
    placa = int(placa)
    ultimo_digito = placa % 10
    match ultimo_digito:
        case 1 | 2:
            print("Segunda feira")
        case 3 | 4:
            print("Terça feira")
        case 5 | 6:
            print("Quarta feira")
        case 7 | 8:
            print("Quinta feira")
        case 9 | 0:
            print("Sexta feira")
else:
    print("Placa digitada inválida!")