"""
Exercicios:
1. Dada uma nota, verificar se ela é válida(entre 0 e 10 inclusive)
2. Dadas duas notas, calcular a média e verificar se está aprovado ou reprovado. média 6.
3. Dadas 3 notas, descartar a menor e calcular a media simples das outras duas e verificar se está aprovado ou reprovado com média >= 6.
"""

# Ex - 01
# notaExercicio1 = float(input("Digite sua nota: "))

# if notaExercicio1 >= 0 and notaExercicio1 <= 10:
#     print(f'A nota {notaExercicio1} é válida!')
# else:
#     print(f'A nota {notaExercicio1} é inválida!')

# # Ex - 02
# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input("Digite sua segunda nota: "))
# media = (nota1 + nota2) / 2

# if media >= 6 :
#     print(f'Aluno aprovado com média maior que 6: {media}')
# else:
#     print(f'Media abaixo de 6, aluno reprovado.')

# Ex- - 03
ex03_nota1 = float(input("Digite sua nota: "))
ex03_nota2 = float(input("Digite sua nota: "))
ex03_nota3 = float(input("Digite sua nota: "))

menor = ex03_nota1

if menor > ex03_nota2:
    menor = ex03_nota2

if menor > ex03_nota3:
    menor = ex03_nota3

media = (ex03_nota1 + ex03_nota2 + ex03_nota3 - menor) / 2

if media >= 6 :
    print(f'Aluno aprovado com média maior que 6: {media}')
else:
    print(f'Media abaixo de 6, aluno reprovado.')