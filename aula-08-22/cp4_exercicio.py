"""
Definição da atividade:

Utilizando os conceitos aprendidos até então, crie uma prova eletrônica com 5
questões sendo 3 alternativas cada.

REQUISITOS:

- Assim que a questão for respondida já apresentar se o usuário acertou ou errou.

- Ao finalizar a prova, apresentar a quantidade e a porcentagem de acertos.

"""

# Cabeçalho com o nome dos integrantes da dupla
# Aluno 1: Vinícius

# Lista de questões com alternativas e a resposta correta
questoes = [
    {
        'pergunta': 'Qual é a capital da França?',
        'alternativas': ['a) Londres', 'b) Paris', 'c) Roma'],
        'resposta_correta': 'b'
    },
    {
        'pergunta': 'Qual é o resultado de 5 + 3?',
        'alternativas': ['a) 5', 'b) 8', 'c) 7'],
        'resposta_correta': 'b'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa?',
        'alternativas': ['a) Leonardo da Vinci', 'b) Van Gogh', 'c) Picasso'],
        'resposta_correta': 'a'
    },
    {
        'pergunta': 'Em qual planeta vivemos?',
        'alternativas': ['a) Marte', 'b) Júpiter', 'c) Terra'],
        'resposta_correta': 'c'
    },
    {
        'pergunta': 'Qual é a capital do Brasil?',
        'alternativas': ['a) São Paulo', 'b) Rio de Janeiro', 'c) Brasília'],
        'resposta_correta': 'c'
    }
]

# Variáveis para rastrear acertos
acertos = 0

# Loop pelas questões
for i, questao in enumerate(questoes):
    print(f"Questão {i + 1}: {questao['pergunta']}")
    for alternativa in questao['alternativas']:
        print(alternativa)
    resposta_usuario = input("Escolha a alternativa (a/b/c): ").lower()

    # Verifica se a entrada é válida
    while resposta_usuario not in ['a', 'b', 'c']:
        print("\nEntrada inválida. Por favor, escolha uma das alternativas: a, b, ou c.")
        resposta_usuario = input("Escolha a alternativa (a/b/c): ").lower()
    
    if resposta_usuario == questao['resposta_correta']:
        print("Você acertou!\n")
        acertos += 1
    else:
        print(f"Você errou! A resposta correta era '{questao['resposta_correta']}'.\n")

# Cálculo da porcentagem de acertos
percentual_acertos = (acertos / len(questoes)) * 100

# Exibindo o resultado final
print(f"Você acertou {acertos} de {len(questoes)} questões.")
print(f"Percentual de acertos: {percentual_acertos:.2f}%")
