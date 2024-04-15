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
    - quantos tiraram a media final maxima (nota 10)"""
    
import os
os.system('cls')

alunosAprovados = 0
alunosReprovados = 0
alunosNotaMaxima = 0



# Pede notas de CheckPoint, Challenge e Global Solution de 10 alunos.
for i in range(0, 1, 1):
    print("***Notas Checkpoint***")
    # Pede a primeira nota
    cp1 = float(input("1° Nota Checkpoint: "))
    #Enquanto a nota estiver fora de 0 a 10, gera um erro e pede novamente a nota
    while cp1 < 0 or cp1 > 10 or cp1.numeric() == False: 
        print("Erro! Digite uma nota entre 0 e 10")
        cp1 = float(input("1° Nota Checkpoint: "))
        
    # Pede a segunda nota
    cp2 = float(input("2° Nota Checkpoint: "))
    #Enquanto a nota estiver fora de 0 a 10, gera um erro e pede novamente a nota
    while cp2 < 0 or cp2 > 10:
        print("Erro! Digite uma nota entre 0 e 10")
        cp2 = float(input("2° Nota Checkpoint: "))

    # Pede a terceira nota
    cp3 = float(input("3° Nota Checkpoint: "))
    #Enquanto a nota estiver fora de 0 a 10, gera um erro e pede novamente a nota
    while cp3 < 0 or cp3 > 10:
        print("Erro! Digite uma nota entre 0 e 10")
        cp3 = float(input("3° Nota Checkpoint: "))
        
    # Define qual a menor nota
    menorCP = cp1
    if cp2 < menorCP:
        menorCP = cp2
    if cp3 < menorCP:
        menorCP = cp3

    #  Calcula a média simples das duas maiores notas.
    mediaCP = (cp1 + cp2 + cp3 - menorCP) / 2
    
    #  Calcula a média ponderada do Checkpoint (peso 20%)
    mediaPonderadaCP = mediaCP * 0.2
    
    #  Verifica se o aluno está aprovado no Checkpoint com média maior que 5
    if mediaCP >= 6:
        print(f"Checkpoint aprovado com média: {mediaCP}")    
    elif mediaCP < 6:
        print(f"Checkpoint reprovado com média: {mediaCP}")
        
    #  print(f"Media Checkpoint ponderada: {mediaPonderadaCP}") Mostrar no final

    print("\n***Notas Challenge***")
    #  Pede a primeira nota
    challenge01 = float(input("Nota da 1° Sprint: "))
    
    #  Enquanto a nota estiver fora de 0 a 10, gera um erro e pede novamente a nota
    while challenge01 < 0 or challenge01 > 10:
        print("Erro! Digite uma nota entre 0 e 10")
        challenge01 = float(input("Nota da 1° Sprint: "))
    
    # Pede a segunda nota
    challenge02 = float(input("Nota da 2° Sprint: "))
    
    #  Enquanto a nota estiver fora de 0 a 10, gera um erro e pede novamente a nota
    while challenge02 < 0 or challenge02 > 10:
        print("Erro! Digite uma nota entre 0 e 10")
        challenge02 = float(input("Nota da 2° Sprint: "))
    
    
    #  Calcula a média das duas notas do Challenge
    mediaChallenge = (challenge01 + challenge02) / 2 
    
    #  Verifica se o aluno foi aprovado no Challenge com média maior que 5
    if mediaChallenge >= 6:
        print(f"Challenge aprovado com média {mediaChallenge}")
    else:
        print(f"Challenge reprovado com média {mediaChallenge}")
        
    #  Calcula a média ponderada do Challenge (peso 20%)
    mediaPonderadaChallenge = mediaChallenge * 0.2
    
    # print(f"Media Challenge ponderada: {mediaPonderadaChallenge}") Mostrar no final
    
    print("\n***Nota Global Solution***")
    #  Pede nota da Global Solution
    notaGlobalSolution = float(input("Nota da Global Solution: "))
    
    # Verifica se aluno está aprovado na Global Solution com nota acima de 5:
    if notaGlobalSolution >= 6:
        print(f"Global Solution aprovada com nota: {notaGlobalSolution}")
    else:
        print(f"Global Solution reprovada com nota: {notaGlobalSolution}")
    
    #  Calcula média ponderada da Global Solution (peso 60%)
    notaPonderadaGlobalSolution = notaGlobalSolution * 0.6
    
    # Calcula a nota final com as médias e notas ponderadas com seu peso
    notaFinal = notaPonderadaGlobalSolution + mediaPonderadaChallenge + mediaPonderadaCP
    
    # Conta quantos alunos foram aprovados, reprovados e quantos foram aprovados com nota 10
    if notaFinal >= 6:
        alunosAprovados += 1
    elif notaFinal < 6:
        alunosReprovados += 1
    if notaFinal == 10:
        alunosNotaMaxima +=1
    
    print("\n****************************NOTAS FINAIS PONDERADAS: ****************************")
    print(f"Média Checkpoint ponderada: {mediaPonderadaCP:.2f}")
    print(f"Média Challenge ponderada: {mediaPonderadaChallenge:.2f}")
    print(f"Nota Global Solution ponderada: {notaPonderadaGlobalSolution:.2f}")
    print(f"Nota Final: {notaFinal}")
    print("**********************************************")
    if notaFinal >= 6:
        print(f"Aluno(a) aprovado(a) com nota final : {notaFinal:.1f}")
    else:
        print(f"Aluno(a) reprovado(a) com nota final: {notaFinal:.1f}")
    
    # print(f"Nota Global Solution ponderada: {notaPonderadaGlobalSolution}") Mostrar no final
    
print("**********************************************\n")
print(f"""
Número de alunos aprovados: {alunosAprovados}
Número de alunos reprovados: {alunosReprovados}
Número de alunos com nota final 10: {alunosNotaMaxima}
      """)
