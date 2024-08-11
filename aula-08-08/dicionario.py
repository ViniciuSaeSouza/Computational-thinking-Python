import os

# dicionario = {
#     "nome" : "Edson",
#     "idade" : 50
# }

# os.system('cls')

# print(dicionario)

# dicionario2 = dict()
# print(dicionario2)

# chave = input("nome: ")

# dicionario2["nome"] = input('Nome: ')
# dicionario2["idade"] = int(input('Idade: '))
# dicionario2["Idade"] = int(input('Idade: '))

# del dicionario2('idade')

# print(dicionario2)

"""
Crie em dicionario no formato:
notas = {
    "Edson" : 10,
    "Maria" : 5,
}

e faça as seguintes funcionalidades: 

1 - SAIR
2 - Adicionar novo Aluno | Nota (limite de 10 alunos)
3 - Editar Aluno | Nota
4 - Excluir um aluno
5 - Calcular a média da turma
6 - Apagar todos os alunos da turma 
7 - ----
8 - Listar a turma
"""

notas = {
    "saes" : 10.0,
    "larissa" : 9.0
}

# Função responsável por adicionar um novo aluno e sua respectiva nota ao dicionario notas.
def adicionar_novo_aluno_e_nota() -> None:
    os.system('cls')
    print("Adicionando aluno e nota: ")
    while True:
        nome = input("(M - voltar ao menu) Nome: ").lower()
        if nome == "m":
            menu()
            break
        try:
            int(nome)
            print("Nome inválido(numérico)")
        except:
            if nome in notas:
                print("Nome do aluno já existe.")
            else:
                while True:
                    nota = input("(M - voltar ao menu) Nota:")
                    if nota.lower() == "m":
                        menu()
                        break
                    elif nota.isnumeric():
                        nota = float(nota)
                        if 0 < nota <= 10:
                            notas[nome] = nota
                            menu()
                            break
                        else:
                            print("Nota inválida.")
                    else:
                        print("Nota inválida.")      
                        
    # nota = input("Nota (M - voltar ao menu): ")
    
    # if not nota.isnumeric():
    #     if nota.lower() == "m":
    #         menu()
    #     print("Nota inválida(não numérico).")
    #     nota = input("Digite a nota novamente (M - voltar ao menu): ")
    # elif 0 > nota > 10:
    #     print("Nota inválida (0 até 10 apenas).")
    #     nota = input("Digite a nota novamente (M - voltar ao menu): ")
    # else:
    #     notas[nome] = nota
    #     menu()
        
        
    # match nome:
    #     case "m":
    #         menu()
    #     case _:
    #         while True:    
    #             nota = input("Nota (M - voltar ao menu): ").lower()
    #             if nota == "m":
    #                 menu()
    #             elif nota != 
    #             try:
    #                 nota = float(nota)    
    #                 break
    #             except:
    #                 print("Nota inválida(não numérico).")
    #                 nota = input("Digite a nota novamente (M - voltar ao menu): ")
    #                 nota = float(nota)

    #             match nota:
    #                 case 0:
    #                     menu()
                        
    #                 case _:
    #                     nota = float(nota)
    #                     while nota < 0 or nota > 10:
    #                         print("Nota inválida(apenas notas de 0 a 10).")
    #                         nota = float(input("Digite a nota novamente (M - voltar ao menu): "))        
                
    #             notas[nome] = nota
    #             print(notas)


def editar_aluno_e_nota():
    os.system('cls')
    print("- EDITAR ALUNO E NOTA -\n")
    lista_nomes_e_notas()
    
    while True:
        nome_escolhido = input("\nAlterar nome: ").lower()
        if nome_escolhido not in notas:
            print("Erro! Nome não cadastrado.")
        else:
            nome_novo = input("\nNovo nome: ").lower()
            confirmar_novo_nome = input(f"Alterar '{nome_escolhido.capitalize()}' por '{nome_novo.capitalize()}'? \nS - sim \nN - não \nEscolha: ").lower()
            match confirmar_novo_nome:
                case "s":
                    notas[nome_novo] = notas.pop(nome_escolhido)
                    os.system('cls')
                    print("Nome alterado com sucesso!")
                    voltar_pro_menu()
                    break
                case "n":
                    print("Nome não alterado")
                    voltar_pro_menu()
                    break
    

def lista_nomes_e_notas():
    print("Nomes e notas cadastradas: \n")
    for nome, nota in notas.items():
        print(f"{nome}: {nota}")
    

def voltar_pro_menu():
    while True:
        voltar_menu = input("\nVoltar ao menu ou sair? M - menu S - sair \nEscolha: ")
        if voltar_menu.lower() == "m":
            menu()
            break
        elif voltar_menu.lower() =="s":
            break
        else:
            print("Erro! Opção inválida.")

def menu() -> None:
    os.system('cls')
    print("""- MENU NOTAS -
1 - Listar a turma
2 - Adicionar novo Aluno | Nota
3 - Editar Aluno | Nota
4 - Excluir um aluno
5 - Calcular média da turma
6 - Apagar todos os alunos da turma
7 - SAIR
""")
    
    escolha = input("Digite a opção: ")
    match escolha:
        case "1":
            os.system('cls')
            lista_nomes_e_notas()
            voltar_pro_menu()
        case "2":
            adicionar_novo_aluno_e_nota()
        case "3":
            editar_aluno_e_nota()
            
        case "7":
            exit()
            


menu()