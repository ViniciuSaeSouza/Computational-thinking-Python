"""
Caso a pessoa fique em exame, pedir a nota de exame e recalcular a media simples (exame com a media), se a nova media for maior ou igual a 6, o aluno está aprovado em exame, caso contrário, reprovado em exame. Em ambos os casos, ebixir a media final
"""

nota1 = float(input("Nota 1: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Nota 3: "))
        if nota3 >= 0 and nota3 <= 10:
            # verificar qual a menor
            menor = nota1
 
            if nota2 < menor:
                menor = nota2
 
            if nota3 < menor:
                menor = nota3
 
            # Calcular a média
            media = (nota1 + nota2 + nota3 - menor) / 2
            
            if media >= 6:
                print(f"Aprovado {media}")
            elif media < 4:
                print(f"Reprovado {media}")
            else:
                print(f"Exame {media}")
                notaExame = float(input(f"\nDigite a nota do exame: "))
                mediaExame = (notaExame + media) / 2
                if mediaExame >= 6:
                    print(f"Aluno aprovado em exame, com media final: ", mediaExame)
                else:
                    print(f"Aluno reprovado em exame, com media final: ", mediaExame)
 
        else:
            print(f"Nota inválida: '{nota3}'")
    else:
        print(f"Nota inválida: '{nota2}'")
else:
    print(f"Nota inválida: '{nota1}'")
    
