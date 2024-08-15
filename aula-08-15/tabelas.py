import os
os.system('cls')

def exibe_tabela(t: list) -> None:
    for i in range(0, len(tabela), 1):
        print(f"Registro {i+1}")
        print(f"Nome....: {t[i]['nome']}")
        print(f"Idade...: {t[i]['idade']}\n")

tabela = list()

contato = {
    'nome' : 'Edson',
    'idade' : 50,
}

# Criando uma nova chave (key) e valor (value)
contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))

tabela.append(contato.copy()) # copy() cria uma referência em outro espeaço de memória

contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))

tabela.append(contato.copy())
print("Tabela: \n", tabela)

exibe_tabela(tabela)



# excluir uma chave - 2 maneiras
# contato.pop('email')
# del contato['email']

# print(contato)

