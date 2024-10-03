# RM 554456 - VINÍCIUS SAES DE SOUZA

import os

# SUB-ALGORITMOS

def valida_credencial(dado: str, tipo: str) -> bool:
    letras = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    letras = letras.split(",")
    dado = dado.lower()
    if tipo == 'l':
        if len(dado) != 6:
            return False
        elif not dado[0].isnumeric():
            return False
        flag = False
        for char in dado[1:]:
            if char in letras:
                flag = True
        if flag == False:
            return False
        else:
            return True

    if tipo == 's':
        if len(dado) < 6:
            return False
        elif dado[0] not in letras:
            return False
        
        flag = False
        for char in dado[1:]:
            if char.isnumeric():
                flag = True
        
        if flag == False:
            return False
        else:
            return True

def cadastrar_credencial() -> None:
    os.system('cls')
    while True:
        login = input("Login: ")
        if valida_credencial(login, 'l'):
            break
        else:
            print("ERRO! Digite um login válido")
    while True:
        senha = input("Senha: ")
        if valida_credencial(senha, 's'):
            print("\nLogin e Senha cadastrado com sucesso!")
            cria_arquivo(login, senha)
            input("Digite qualquer tecla para voltar: ")
            menu()
            break
        else:
            print("ERRO! Digite uma senha válida")

def cria_arquivo(login: str, senha: str) -> None:
    with open("rm554456.txt", "a") as file:
        pessoa = f"{login.upper()}, {senha}\n"
        file.write(pessoa)

def mostrar_arquivo():
    with open("rm554456.txt", "r", encoding="utf-8") as file:
        os.system('cls')
        print(file.read())
        input("Digite qualquer tecla para voltar ao menu: ")
        menu()


# MAIN
def menu():
    os.system('cls')
    print("""MENU
0 - SAIR
1 - Digite as credenciais (Login e Senha)
2 - Exibir o arquivo""")

    escolha = input("Escolha: ")

    while (True):
        match escolha:
            case "0":
                print("Fechando programa...")
                exit()
            case "1":
                cadastrar_credencial()
            case "2":
                mostrar_arquivo()
            case _:
                print("Escolha uma opção válida!")
                menu()

menu()

"""
34MARI, maria23!
8483ES, mac3435
5EDSON, abc12345
"""