import os
os.system('cls')
candidatos = [0, 0, 0, 0]
votos_candidato = [0, 0, 0, 0]
total_votos = 0
print("Digite o nome dos candidatos: ")
candidatos[0] = input("1: ")
candidatos[1] = input("2: ")
candidatos[2] = input("3: ")
candidatos[3] = "NULOS"

os.system('cls')
print(f"""
CANDIDATOS
1- {candidatos[0]}
2- {candidatos[1]}
3- {candidatos[2]}
0 - FIM DA VOTAÇÃO
""")

voto = int(input("VOTO: "))
if voto == 1:
        total_votos += 1
        votos_candidato[0] += 1
elif voto == 2:
        total_votos +=1
        votos_candidato[1] += 1
elif voto == 3:
        total_votos += 1
        votos_candidato[2] += 1
elif voto >= 4 or voto < 0:
      total_votos += 1
      votos_candidato[3] += 1

while voto != 0:
    print(f"""
CANDIDATOS

1- {candidatos[0]}
2- {candidatos[1]}
3- {candidatos[2]}
0 - FIM DA VOTAÇÃO \n
""")
    voto = int(input("VOTO: "))
    if voto == 1:
        total_votos += 1
        votos_candidato[0] += 1
    elif voto == 2:
        total_votos +=1
        votos_candidato[1] += 1
    elif voto == 3:
        total_votos += 1
        votos_candidato[2] += 1
    elif voto >= 4 or voto < 0:
      total_votos += 1
      votos_candidato[3] += 1

if total_votos == 0:
     total_votos_final = 1
else:
     total_votos_final = total_votos

os.system('cls')
print(f"""
CANDIDATOS
TOTAL DE VOTOS: {total_votos}
1 - {candidatos[0]}\t->{votos_candidato[0]} votos \t->{(votos_candidato[0] * 100) / total_votos_final:.2f}%
2 - {candidatos[1]}\t->{votos_candidato[1]} votos \t->{(votos_candidato[1] * 100) / total_votos_final:.2f}%
3 - {candidatos[2]} \t->{votos_candidato[2]} votos \t->{(votos_candidato[2] * 100) / total_votos_final:.2f}%
    {candidatos[3]}\t->{votos_candidato[3]} votos \t->{(votos_candidato[3] * 100) / total_votos_final:.2f}%
""")