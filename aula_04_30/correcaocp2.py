import os
os.system('cls')

# ----- Cadastrar os candidatos

candidatos = ['', '', '']

print("Digite os nomes dos candidatos: ")

for i in range(3):
    candidatos[i] = input(f"{i+1}. ")
    
# ----- Votação
cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0

while True:
    print(f'''
CANDIDATOS

1 - {candidatos[0]}
2 - {candidatos[1]}
3 - {candidatos[2]}
0 - FIM DA VOTAÇÃO     
''')
    voto = int(input(' ' * 4+"VOTO: "))
    
    match voto:
        case 0:
            break
        case 1:
            cand1 = cand1 + 1
        case 2:
            cand2 = cand2 + 1
        case 3:
            cand3 = cand3 + 1
        case _:
            nulo = nulo + 1
            
# candidatos[0] = input("1. ")
# candidatos[1] = input("2. ")
# candidatos[2] = input("3. ")