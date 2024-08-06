import os

meu_dict = {
    'nome': '',
    'idade' : 0,
    'altura' : 0,
    'curso' : '',
    'cor_favorita' : ''
}

def preenche_dicionario(dicionario: dict) -> None:
    print('Preencha as informações abaixo!')
    for k in dicionario.keys():
        dicionario[k] = input(f"{k}: ")
        

def exibe_dict_manualmente(dicionario: dict) -> None:
    print("\nDICIONÁRIO EXIBIDO MANUALMENTE")
    print(f"Nome...: {dicionario['nome']}")
    print(f"Idade...: {dicionario['idade']}")
    print(f"Altura...: {dicionario['altura']}")
    # print(f"Curso...: {dicionario['curso']}")
    print(f"Cor favorita...: {dicionario['cor_favorita']}")

def exibe_dict_por_metodo(dicionario: dict) -> None:
    print("\nDICIONÁRIO EXIBIDO POR MÉTODO")
    for k, v in dicionario.items():
        print(f"{k}...: {v}")
        
def adiciona_key_value(dicionario: dict) -> None:
    k = input("Digite uma key: ")
    dicionario[k] = input(f"{k}...: ")

def remove_key(dicionario: dict) -> None:
    k = input("Remover chave: ")
    del dicionario[k]

preenche_dicionario(meu_dict)
adiciona_key_value(meu_dict)
remove_key(meu_dict)
exibe_dict_manualmente(meu_dict)
exibe_dict_por_metodo(meu_dict)

# Exercício, fazer um subalgoritmo que acrescente uma key no dicionário
# Exercicio, fazer um subalgoritmos que remova uma key no dicionario