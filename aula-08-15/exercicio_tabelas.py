import os
"""
Crie um dicionário com 5 keys e faça um sistema com a seguinte sugestão de menu:

0 - Sair
1 - Cadastrar
2 - Consultar 
3 - Alterar
4 - Excluir
"""

# Inicia uma lista para inserir o dicionário de pessoa física (virando uma tabela)
tabela_pessoas = list()

#  Cria um dicionário de pessoa física
dict_pessoa_fisica = {
    'cpf' : str,
    'nome' : str,
    'idade' : int,
    'altura' : float,
    'sexo' : str
}

def voltar_menu():
    input("\nDigite qualquer tecla para voltar ao menu: ")
    menu()

def cadastrar_pessoa():
    cpf = input("Digite o cpf: ")
    if verifica_cpf_cadastrado(cpf):
        print("CPF já cadastrado no sistema!")
        voltar_menu()
    else:
        dict_pessoa_fisica['cpf'] = cpf
        dict_pessoa_fisica['nome'] = input("Nome: ")
        dict_pessoa_fisica['idade'] = input("Idade: ")
        dict_pessoa_fisica['altura'] = input("Altura: ")
        dict_pessoa_fisica['sexo'] = input("Sexo: ")
        
    tabela_pessoas.append(dict_pessoa_fisica.copy())
    print("Cadastro realizado com sucesso!")
    voltar_menu()
    


def lista_cpfs_cadastrados() -> None:
    print(" --CPF CADASTRADOS-- ")
    for i in range(0,len(tabela_pessoas),1):
        print(tabela_pessoas[i]['cpf'])
        
def verifica_cpf_cadastrado(cpf: str) -> bool:
   for pessoa in tabela_pessoas:
        if pessoa['cpf'] == cpf:
            return True
        else:
            return False

def consultar():
    lista_cpfs_cadastrados()
    cpf_consulta = input("Digite o cpf que quer consultar: ")
    if verifica_cpf_cadastrado(cpf_consulta):
        os.system('cls')
        for pessoa in tabela_pessoas:
            if cpf_consulta == pessoa['cpf']:
                print(f"""
    Dados da pessoa:
CPF: {pessoa['cpf']} 
Nome: {pessoa['nome']} 
Idade: {pessoa['idade']} 
Altura: {pessoa['altura']} 
Sexo: {pessoa['sexo']}
    """)
                voltar_menu()
    
    else:
        voltar_menu()
                
def alterar_cadastro():
    lista_cpfs_cadastrados()
    cpf_alterar = input("CPF a ser alterado: ")
    if verifica_cpf_cadastrado(cpf_alterar):
        for i, pessoa in enumerate(tabela_pessoas):
            if pessoa['cpf'] == cpf_alterar:
                tabela_pessoas[i]['cpf'] = input("Novo CPF:")
                tabela_pessoas[i]['nome'] = input("Nome: ")
                tabela_pessoas[i]['idade'] = input("Idade: ")
                tabela_pessoas[i]['altura'] = input("Altura: ")
                tabela_pessoas[i]['sexo'] = input("Sexo: ")
                voltar_menu()
    else:
        print("ERRO! cpf digitado incorreto.")
        voltar_menu()
    
def excluir_cadastro():
    lista_cpfs_cadastrados()
    cpf_excluir = input("CPF para ser excluído: ")
    if verifica_cpf_cadastrado(cpf_excluir):
        for i, pessoa in enumerate(tabela_pessoas):
            if pessoa['cpf'] == cpf_excluir:
                os.system('cls')
                print("Usuário deletado com sucesso!")
                del tabela_pessoas[i]
                lista_cpfs_cadastrados()
                voltar_menu()
    else:
        print("ERRO! CPF não cadastrado.")
        voltar_menu()
                


#  Exibe menu principal
def menu():
    os.system('cls')
    print("""
0 - Sair
1 - Cadastrar
2 - Consultar 
3 - Alterar
4 - Excluir
""")
    escolha = input("Escolha: ")
    match escolha:
        case '0':
            print("Finalizando o programa!")
            exit()
        case '1':
            cadastrar_pessoa()
        case '2':
            consultar()
        case '3':
            alterar_cadastro()
        case '4':
            excluir_cadastro()

menu()
