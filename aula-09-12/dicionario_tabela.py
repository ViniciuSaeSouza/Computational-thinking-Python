# RM 554456 - VINICIUS SAES DE SOUZA
# RM 557002 - ANDERSON DE SOUSA PEDRO

"""
Instruções
ASSUNTO: Dicionário e Tabela | Dicionário: contato (cpf, nome e idade).

Ao digitar o CPF, se ele não existir, pedir a digitação dos outros dois campos e cadastrar o registro, finalizando
com "Cadastrado com sucesso!". Se ao digitar o CPF ele existir, apresentar o registro inteiro e permitir que o
usuário edite o nome e idade; caso a digitação seja nula, manter o dado anterior, se digitar algo, substituir,
finalizando com "Editado com sucesso!".Para encerrar o programa, deixar o CPF em branco, deverá aparecer:
"Programa finalizado".
Exemplo da execução:

CPF: 12312312312
Nome: Edson
Idade: 40
Cadastrado com sucesso!

CPF: 12312312312
CPF: 12312312312
Nome: Edson
Idade: 40

Nome: Edson de Oliveira
Idade: -> A idade permaneceu 40
Editado com sucesso!

CPF:
Programa finalizado!

"""

contatos = {'contato_1' : {'cpf':'445', 'nome': 'larissa', 'idade': '18'}}

def editar_informacao(cpf:str):
    for pessoa , dados in contatos.items():
        if dados['cpf'] == cpf:
            print(f"CPF: {dados['cpf']}\nNome: {dados['nome']}\nIdade: {dados['idade']}")
            
            nome = input("Nome: ")
            if nome != "":
                dados['nome'] = nome
            
            idade = input("Idade: ")
            if idade != "":
                dados['idade'] = idade
    print("Editado com sucesso!")

def verifica_cpf_existente(cpf:str) -> bool:
    for k, v in contatos.items():
        if cpf in v.values():
            return True
    return False

def funcao_principal() -> None:
    cpf = input("CPF: ")
    if cpf == "":
        print("Programa finalizado")
        exit()
    elif verifica_cpf_existente(cpf):
        editar_informacao(cpf)
    else:
        nome = input("Nome: ").lower()
        idade = input("Idade: ").lower()
        contatos[f"contato_{len(contatos)+1}"] = {'cpf':cpf, 'nome': nome, 'idade':idade}
        print("Cadastrado com sucesso!")
    funcao_principal()
    

funcao_principal()