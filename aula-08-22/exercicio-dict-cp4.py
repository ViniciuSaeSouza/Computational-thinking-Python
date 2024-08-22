# Guilherme Francisco     - RM 557648
# Vinicius Saes de Souza  - RM 554456

import os
# Dicionário com 5 perguntas, cada pergunta possui: enunciado, alternativas , resposta_certa. É devolvido um contador(int) que armazena o número de acertos.
prova = {
    'Pergunta 1' : {
        'enunciado' : 'Qual a capital da frança?', 
        'alternativas' : {
            'a':'Xique-Xique',
            'b':'Brás',
            'c':'Paris',
        },
        'resposta_certa':'c'
    },
    'Pergunta 2' : {
        'enunciado' : 'Quantas cores tem o arco-íris?',
        'alternativas' : {
            'a':'7',
            'b':'8',
            'c':'9',
        },
        'resposta_certa':'a'
    },
    'Pergunta 3' : {
        'enunciado' : 'Qual desses animais vive na água?',
        'alternativas' : {
            'a' : 'Tigre',
            'b' : 'Tubarão',
            'c' : 'Papagaio',
        },
        'resposta_certa' : 'b'
    },
    'Pergunta 4' : {
        'enunciado' : 'Quantos planetas existem no sistema solar?',
        'alternativas' : {
            'a' : '8',
            'b' : '9',
            'c' : '7',
        },
        'resposta_certa' : 'a'
    },
    'Pergunta 5' : {
        'enunciado' : 'Qual o maior continente em termos de área?',
        'alternativas' : {
            'a' : 'Oceania',
            'b' : 'Europa',
            'c' : 'Ásia'
        },
        'resposta_certa' : 'c'
    }
}

# Exibe título (passado como parâmetro) com borda superior e inferior de * com o tamanho respectivo ao tamanho do título.
def exibe_titulo(texto:str):
    tamanho = len(texto)
    print('*' * tamanho)
    print(texto.upper())
    print('*' * tamanho)
    
def exibe_enunciado(enun: str):
    tamanho = len(enun)
    print(enun.capitalize())
    print('-' * tamanho)
    

# Exibe enunciado e alternativas de cada pergunta dentro do dicionário provas, armazena e devolve o número de acertos na variável 'contador'(int)
def exibe_e_responde_prova(prova: dict) -> int:
    os.system('cls')
    contador = 0
    for perguntas in prova.values():
        exibe_enunciado(perguntas['enunciado'])
        for letra in perguntas['alternativas']:
            print(f"{letra}) {perguntas['alternativas'][letra]}")
        resposta = input("Resposta: ").lower()
        if resposta == perguntas['resposta_certa']:
            print("Acertou!\n")
            contador += 1
        else:
            print("Errou!\n")
    return contador

# Calcula a taxa de acertos (passada por parâmetro) baseado no tamanho do (dict) prova e imprime na tela
def calcula_taxa_acerto(acertos: int):
    taxa_de_acertos = acertos / len(prova) * 100
    print(f"""
Respostas certas: {acertos}
Taxa de acerto: {taxa_de_acertos:.1f}%
""")

def main():
    os.system('cls')
    exibe_titulo("prova eletrônica")
    input("Digite qualquer tecla para iniciar a prova: ")
    acertos = exibe_e_responde_prova(prova)
    calcula_taxa_acerto(acertos)

main()