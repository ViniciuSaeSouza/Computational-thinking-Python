# Guilherme Francisco     - RM 557648
# Vinicius Saes de Souza  - RM 554456

import os

taxa_acerto = []
nome = []

perguntas = {
    'Pergunta 1' : {
        "pergunta" : "Qual a capital da frança?", 
        "resposta" : {
                    'a':'1',
                    'b':'2',
                    'c':'3'},
        'resposta_certa':'b'},
    'Pergunta 2' : {
        'pergunta' : 'Quantas cores tem o arco-íris?',
        'resposta' : {'a':''}
    },
    2 : "Quantas cores tem no arco-íris?",
    3 : "Qual desses animais vive na água?",
    4 : "Quantos planetas existem no sistema solar?",
    5 : "Qual o maior continente em termos de área? "
}



def exibe_titulo(t: str):
    tamanho = len(t)
    print('*' * tamanho)
    print(t.upper())
    print('*' * tamanho)


def cadastra_nome():
    exibe_titulo("cadastra nome")
    nome_cadastro = input("Digite seu nome: ")
    nome.append(nome_cadastro)


def proxima_pergunta():
    input("Digite qualquer tecla para a próxima pergunta: ")


def pergunta_um(ct:int):
    os.system('cls')
    exibe_titulo("Primeira pergunta")
    print(perguntas[1])
    print("""
a) Xique-Xique
b) Brás
c) Paris                          
""")
    resp = input("Escolha: ").lower()
    match resp:
        case "a":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_dois(ct)
        case "b":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_dois(ct)
        case "c":
            print("Acertoooou!")
            ct += 1
            taxa_acerto.append(1)
            proxima_pergunta()
            pergunta_dois(ct)
        case _:
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_dois(ct)
                
def pergunta_dois(ct:int):
    os.system('cls')
    exibe_titulo("segunda pergunta")
    print(perguntas[2])
    print("""
a) 7
b) 6
c) 9                          
""")
    resp = input("Escolha: ").lower()
    match resp:
        case "a":
            print("Acertoooou!")
            ct += 1
            taxa_acerto.append(1)
            proxima_pergunta()
            pergunta_tres(ct)
        case "b":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_tres(ct)
        case "c":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_tres(ct)
        case _:
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_tres(ct)

def pergunta_tres(ct:int):
    os.system('cls')
    exibe_titulo("terceira pergunta")
    print(perguntas[3])
    print("""
a) Ornitorrinco
b) Tubarão
c) Onça                          
    """)
    resp = input("Escolha: ").lower()
    match resp:
        case "a":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_quatro(ct)
        case "b":
            print("Acertoooou!")
            ct += 1
            taxa_acerto.append(1)
            proxima_pergunta()
            pergunta_quatro(ct)
        case "c":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_quatro(ct)
        case _:
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_quatro(ct)

def pergunta_quatro(ct:int):
    os.system('cls')
    exibe_titulo("quarta pergunta")
    print(perguntas[4])
    print("""
a) 8
b) 7
c) 10                          
""")
    resp = input("Escolha: ").lower()
    match resp:
        case "a":
            print("Acertoooou!")
            ct += 1
            taxa_acerto.append(1)
            proxima_pergunta()
            pergunta_cinco(ct)
        case "b":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_cinco(ct)
        case "c":
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_cinco(ct)
        case _:
            print("Errrrrouuu!")
            proxima_pergunta()
            pergunta_cinco(ct)

def pergunta_cinco(ct: int) -> int:
    os.system('cls')
    exibe_titulo("quinta pergunta")
    print(perguntas[5])
    print("""
a) Europa
b) América
c) Ásia                          
""")
    resp = input("Escolha: ").lower()
    match resp:
        case "a":
            print("Errrrrouuu!")
        case "b":
           print("Errrrrouuu!")
        case "c":
            print("Acertoooou!")
            taxa_acerto.append(1)
            ct += 1
            return ct
        case _:
            print("Errrrrouuu!")

            
# def atualiza_contador(ct: int) -> int:
    
def exibe_resultados():
    os.system('cls')
    exibe_titulo("resultados")
    print(f"{nome[0]} acertou {len(taxa_acerto)} perguntas de {len(perguntas)} questões.")
    acerto = len(taxa_acerto)/len(perguntas) * 100
    print(f"Sua taxa de acerto foi de: {acerto}%")


def main():
    os.system('cls')
    cadastra_nome()
    pergunta_um(len(taxa_acerto))
    exibe_resultados()
    


main()