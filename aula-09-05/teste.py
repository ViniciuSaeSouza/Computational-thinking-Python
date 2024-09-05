"""
Exercício:
Crie o seguinte menu:
0 - SAIR
1 - GRAVAR O ARQUIVO
2 - LER O ARQUIVO
3 - EDITAR O ARQUIVO
"""
 
import os
os.system('cls')
  
 
def gravar_arquivo():
    nome_arqv = input("Digite o nome do arquivo:_ ")
    conteudo = input("Digite o conteúdo do arquivo: ")
    arquivo = open(nome_arqv, 'w', encoding='utf-8')
    arquivo.write(conteudo + "\n")
    arquivo.close()
    os.system('cls')
    print(f"""Seu arquivo '{nome_arqv}', foi criado com Sucesso!\nE a informação '{conteudo}' foi gravada nele!""")
    input("Digite uma tecla para voltar ao MENU!")
    exibe_menu()

 
 
def ler_arquivo():
    escolha_arquivo = input("Qual arquivo deseja ler? :_")
    try:
        arquivo = open(escolha_arquivo, 'r', encoding='utf-8')
    except FileNotFoundError:
        print("Buurrooooo! Digita o nome certo do arquivo, caraiooo!")
        escolha_arquivo = input("Qual arquivo deseja ler? :_")
        arquivo = open(escolha_arquivo, 'r', encoding='utf-8')
    os.system('cls')
    print(f"Seu arquivo '{escolha_arquivo}' foi aberto: ")
    print(arquivo.read())
    arquivo.close()
    input("Digite uma tecla para voltar ao MENU!")
    exibe_menu()
 
def editar_arquivo():
    editar_arquivo = input("Qual arquivo deseja editar? :_")
    conteudo = input("Conteúdo:_ ")
    try:
        arquivo = open(editar_arquivo, "a", encoding='utf-8')
    except FileNotFoundError:
       print("Buurrooooo! Digita o nome certo do arquivo, caraiooo!")
       editar_arquivo = input("Qual arquivo deseja editar? :_")
       arquivo = open(editar_arquivo, 'a', encoding='utf-8')
       
    arquivo.write(conteudo + "\n")
    arquivo.close()
    os.system('cls')
    print(f"""Seu arquvio '{editar_arquivo}' foi editado!\nAs informações '{conteudo}', foram adicionadas nele!""")
    input("Digite uma tecla para voltar ao MENU!")

    exibe_menu()


def exibe_menu():
    os.system('cls')
    print("""
#####    MENU    #####
          
0 - SAIR
1 - GRAVAR O ARQUIVO
2 - LER O ARQUIVO
3 - EDITAR O ARQUIVO""")  

exibe_menu()
 
while True:
    escolha = input("Escolha uma opção: ")
    match escolha:
        case "0":
            exit()
        case "1":
            gravar_arquivo()
        case "2":
            ler_arquivo()
        case "3":
            editar_arquivo()
        case _:
            print("Digite uma opção válida!")