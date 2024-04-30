"""
Uma turma tem 10 alunos.
Um professor desenvolveu uma rotina para ter um melhor gerenciamento o gerenciamento dos alunos.
A média anual se dá por:
- Checkpoint:
    - São 3 avaliações
    - Calcula-se a média comum das duas maiores notas
    - Vale 20% da média final
- Challenge:
    - São 2 sprints
    - O cálculo é a média simples das duas notas
    - Vale 20% da média final
- Global solution:
    - Apenas uma nota que
    - Vale 60% da média final.
Requisitos:
- A média final para passar é ao menos 6, senão estará reprovado
- Toda vez que for digitada uma nota inválida (fora de 0 e 10), advertir
  e pedir novamente a digitação da mesma nota.
Relatório:
- para cada aluno exibir as médias calculadas e se ele está aprovado ou não.
- no final da digitação das notas dos dez alunos, exibir:
    - quantos foram aprovados
    - quantos foram reprovados
    - quantos tiraram a media final maxima (nota 10)
"""

import os
os.system('cls')

for i in range(1, 11, 1):
    print("Checkpoint: ")
    cp1 = float(input("CP1: "))
    while cp1 < 0 or cp1 > 10:
        print("Erro, digite um número válido entre 0 e 10")
        cp1 = float(input("CP1: "))
        
    
    cp2 = float(input("CP2: "))
    while cp2 < 0 or cp2 > 10:
        print("Erro, digite um número válido entre 0 e 10")
        cp2 = float(input("CP2: "))
    
    cp3 = float(input("CP3: "))
    while cp3 < 0 or cp3 > 10:
        print("Erro, digite um número válido entre 0 e 10")
        cp3 = float(input("CP3: "))

    cpMenor = cp1
    if cp2 < cpMenor:
        cpMenor = cp2
    if cp3 < cpMenor:
        cpMenor = cp3

    mediaCP = ((cp1 + cp2 + cp3) - cpMenor) / 2
    print(f"Media Checkpoint {cp1} + {cp2} + {cp3} - {cpMenor} / 2 = {mediaCP:.2f}")

    print("Challenge: ")
    sp01 = float(input("Nota da 1° Sprint: "))

    while sp01 < 0 or sp01 > 10 or sp01 == str:
        print("Erro! Digite um número válido entre 0 e 10")
        sp01 = float(input("Nota da 1° Sprint: "))