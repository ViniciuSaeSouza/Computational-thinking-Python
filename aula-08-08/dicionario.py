import os

# DÚVIDA - NO DICIONÁRIO EU SÓ VOU CONSEGUIR ARMAZENAR UMA NOTA PARA CADA CHAVE(ALUNO)? OU CONSIGO ADICIONAR UM ARRAY DE NOTAS? COMO EU PERCORRO POR ESSE ARRAY DE NOTAS (UTILIZO UM SEGUNDO 'FOR'?)

"""
Crie um dicionario no formato:
notas = {
    "Edson": 10, - chave: nota do aluno, cabivel estar em maiusculo
    "Maria": 5, - dado float
}

e faça as seguintes funcionalidades:

1 - SAIR
2 - Adicionar novo aluno | Nota (limite de 10 alunos) - usar o for
3 - Editar Aluno | Nota - duas entradas, se o aluno existe eu edito
4 - Excluir um aluno
5 - Calcular a média da turma - método value
6 - Apagar todos os alunos
7 - Consultar um aluno
8 - Listar as notas e os nomes

"""

"""
Nome: Marcelo  - verificar se o nome já existe - gets
Nota: 9
Gravado

cenario2:
Nome: Edson - não gravar o mesmo nome
aparecer um já existe - get

* >= 10 alunos

Cenário 3:
Nome: Maria
Nota: 6
mensagem: gravou

se existir eu passo
se não existir eu gravo

upper - pra deixar maiusculo ou minusculo

nota invalida, voltar pro menu - o nome não ta gravado tbm

"""

notas = {
    "saes" : 10.0,
    "larissa" : 9.0
}

# Função responsável por adicionar um novo aluno e sua respectiva nota ao dicionario notas.
def adicionar_novo_aluno_e_nota() -> None:
    os.system('cls')
    print("- ADICIONANDO ALUNO E NOTA -")
    lista_nomes_e_notas()
    while True:
        if len(notas) > 10:
            print("Turma cheia! Não é possível adicionar mais alunos.")
            voltar_pro_menu()
        nome = input("\nCadastrar Nome: ").lower()
        try:
            int(nome)
            print("Nome inválido(numérico)")
        except:
            if nome in notas:
                print("Nome do aluno já existe.")
            else:
                while True:
                    while True:
                        nota = input(f"Nota de {nome.capitalize()}: ")
                        try:
                            nota = float(nota)
                            break
                        except:
                            print("ERRO! Nota inválida.")
                    if 0 <= nota <= 10:
                        os.system('cls')
                        notas[nome] = nota
                        print("Nome cadastrado com sucesso!")
                        lista_nomes_e_notas()
                        voltar_pro_menu()
                        break
                    else:
                        print("ERRO! Nota deve estar entre 0 e 10.")
                    # else:
                    #     print("Nota inválida.")      
                        
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
    print("- EDITAR ALUNO E NOTA -")
    lista_nomes_e_notas()
    while True:
        nome_escolhido = input("\nAlterar Nome e Nota de: ").lower()
        if nome_escolhido not in notas:
            print("Erro! Nome não cadastrado.")
        else:
            while True:
                nome_novo = input("\nNovo nome: ").lower()
                if nome_novo == '':
                    print("ERRO! Nome não pode ser vazio.")
                else:
                    confirmar_novo_nome = input(f"Alterar '{nome_escolhido.capitalize()}' por '{nome_novo.capitalize()}'? \nS - sim \nN - não \nEscolha: ").lower()
                    match confirmar_novo_nome:
                        case "s":
                            notas[nome_novo] = notas.pop(nome_escolhido)
                            os.system('cls')
                            print("Nome alterado com sucesso!")
                            break
                        case "n":
                            os.system('cls')
                            print("Nome não alterado")
                            break
                        case _:
                            print("ERRO! Opção inválida")
            break
    
    while True: 
        alterar_nota = input(f"\nDeseja alterar a nota de {nome_novo.capitalize()}?\n S - Sim \n N - Não \nEscolha: ").lower()
        match alterar_nota:
            case "s":
                while True:
                    try:
                        nota_nova = float(input("\nNova nota: "))
                        if 0<= nota_nova <= 10:
                            break
                        else:
                            print("ERRO! Insira uma nota entre 0 e 10")
                    except:
                        print("Erro! Insira um número válido")             
                    confirmar_nova_nota = input(f"\nAlterar '{notas[nome_novo]}' por '{nota_nova}'? \nS - sim \nN - não \nEscolha: ").lower()
                    match confirmar_nova_nota:
                        case "s":
                            notas[nome_novo] = nota_nova
                            print("Nota alterada com sucesso!")
                            voltar_pro_menu()
                            break
                        case "n":
                            print("Nota não alterada!")
                        case _:
                            print("ERRO! opção inválida")
            case "n":
                voltar_pro_menu()
            case _:
                print(f"ERRO! Opção digitada {alterar_nota} não é válida.")
                
            
    

def lista_nomes_e_notas():
    print("\nNomes e notas cadastradas: ")
    for nome, nota in notas.items():
        print(f"{nome.capitalize()} - Nota: {nota}")
    
    
    

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
            
def excluir_aluno():
    os.system('cls')
    print("- EXCLUIR ALUNO -\n")
    lista_nomes_e_notas()
    while True:
        nome_para_excluir = input("Digite o nome que quer excluir: ").lower()
        if nome_para_excluir in notas:
            confirmacao = input(f"\nDeseja excluir o cadastro de {nome_para_excluir.capitalize()}?\nS - Sim \nN - Não \nEscolha: ").lower()
            match confirmacao:
                case "s":
                    del notas[nome_para_excluir]
                    print("Nome excluído com sucesso!")
                    voltar_pro_menu()
                    break
                case "n":
                    voltar_pro_menu()
                    break
                case _:
                    print("ERRO! Opção inválida.")
        else:
            print("ERRO! Nome digitado não está cadastrado.")
            
            
def menu() -> None:
    os.system('cls')
    print(f"""
        - MENU NOTAS -
1 - Listar as notas e os nomes
2 - Adicionar novo aluno | Nota (limite de 10 alunos)
3 - Editar Aluno | Nota
4 - Excluir um aluno
5 - Calcular a média da turma
6 - Apagar todos os alunos
7 - Consultar um aluno
8 - SAIR
""")
    while True:
        escolha_menu = input("Digite a opção: ")
        try:
            escolha_menu = int(escolha_menu)
        except:
            print("ERRO! Opção digitada inválida.")
        match escolha_menu:
            case 1:
                os.system('cls')
                lista_nomes_e_notas()
                voltar_pro_menu()
            case 2:
                adicionar_novo_aluno_e_nota()
            case 3:
                editar_aluno_e_nota()
            case 4:
                excluir_aluno()
            
            case 7:
                return
            
            case _:
                print(f"ERRO! Opção digitada '{escolha_menu}' não existe.")
            


menu()