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
    'cpf' : '444.222.888.45',
    'nome' : 'Saes',
    'idade' : 28,
    'altura' : 1.81,
    'sexo' : 'Masculino'
}


def cadastrar_pessoa():
    for k, v in dict_pessoa_fisica:
        dict_pessoa_fisica[k] = input(f"{k.capitalize()}: ")
        # converte_value(dict_pessoa_fisica(dict_pessoa_fisica[k]))
    tabela_pessoas.append(dict_pessoa_fisica)
    

def verifica_cadastro_existente(nome: str) -> bool:
    if nome in dict_pessoa_fisica:
        return True
    else:
        return False

def lista_nomes_cadastrados() -> None:
    print(" --NOMES CADASTRADOS-- ")
    print(dict_pessoa_fisica.get('nome'))
        

def consultar():
    lista_nomes_cadastrados()
    nome_consulta = input("Digite o nome a ser consultado: ")
    if verifica_cadastro_existente(nome_consulta):
        print(dict_pessoa_fisica[nome_consulta])
    else:
        print("Nome da pessoa não existe\n")
        menu()
        
    

#  Exibe menu principal
def menu():
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

menu()
