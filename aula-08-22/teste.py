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
print(len(prova))

# for perguntas in prova.values():
#   contador = 0
#   print(perguntas['enunciado'])
#   for letra in perguntas['alternativas']:
#     print(f"{letra}) {perguntas['alternativas'][letra]}")
#   resposta = input("Resposta: ").lower()
#   if resposta == perguntas['resposta_certa']:
#     print("Acertou!")
#     contador += 1
#   else:
#     print("Errou!\n")

#   # for pergunta in perguntas:
#   #   print(f"{pergunta}) {pergunta['alternativas'][pergunta]}")
    
    
#   # for k, v in pergunta.items():
#   #   enunciado = pergunta.get('pergunta')
#   #   print("Value: ", v)
  