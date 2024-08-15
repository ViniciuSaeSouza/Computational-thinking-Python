import os
os.system("cls")

def exibe_tabela(t: list) -> None:
    print("Exibindo:")
    for i in range(0,len(tabela), 1):
        print(f"Registro {i+1}:")
        print(f"Nome....: {t[i]['nome']}")
        print(f"Idade...: {t[i]['idade']}\n")


tabela = list()
contato = {
    'nome': 'Edson',
    'idade': 50,
}

contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))
tabela.append(contato.copy())

contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))
tabela.append(contato.copy())



exibe_tabela(tabela)


'''
# criando uma chave - key
contato['email'] = 'prof@fiap.com.br'
contato['idade'] = int(input("Idade: "))
#contato.pop('email')
#del contato['email']
print(contato)
'''