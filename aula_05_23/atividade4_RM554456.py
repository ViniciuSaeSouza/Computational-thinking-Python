#RM 554456 -  Vinicius Saes de Souza

import os

contador = [0,0,0]

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def intervalo():
    
    limpa_tela()
    print("INTERVALO")
    n1 = int(input("Primeiro número: "))
    n2 = int(input('Segundo número: '))

    maior = n1
    menor = n2
    if n2 > maior:
        maior = n2
        menor = n1
    print('[', end='') 
    for n in range(menor, maior+1, 1):
        print(f'{n}', end = ' ')
    print(']')

    contador[0] +=1

    match input("Pressione qualquer tecla para voltar ao menu: "):
        case _:
            main()


def finalizar_programa():
    limpa_tela()
    def exibir_execucao():
        print(f'''1 - Intervalo - {contador[0]} vez(es)
2 - Intervalo Aberto e Fechado - {contador[1]} vez(es)
3 - Intervalo em ordem crescente ou decrescente - {contador[2]} vez(es)
        ''')
    exibir_execucao()

def intervalo_aberto_fechado():
    limpa_tela()
    print("INTERVALO ABERTO OU FECHADO")
    n1 = int(input("Primeiro número: "))
    n2 = int(input('Segundo número: '))
    aberto_fechado = input('][ - Aberto ou [] Fechado? ][\nEscolha: ')
    match aberto_fechado:
        case '[]':
            maior = n1
            menor = n2
            if n2 > maior:
                maior = n2
                menor = n1
            print('[', end = '') 
            for n in range(menor, maior+1, 1):
                print(f'{n}', end = ' ')
            print(']')
        case '][':
            maior = n1
            menor = n2
            if n2 > maior:
                maior = n2
                menor = n1
            print(']', end='') 
            for n in range(menor+1, maior, 1):
                print(f'{n}', end = ' ')
            print('[')
    contador[1] += 1
    match input("Pressione qualquer tecla para voltar ao menu: "):
        case _:
            main()

def intervalo_cres_decres():
    limpa_tela()
    print('INTERVALO CRESCENTE OU DECRESCENTE')
    n1 = int(input("Primeiro número: "))
    n2 = int(input('Segundo número: '))
    if n2 < n1:
        print('[', end = '') 
        for n in range(n1, n2-1, -1):
            print(f'{n}', end = ' ')
        print(']')    
    else:
        print('[', end = '') 
        for n in range(n1, n2+1, 1):
            print(f'{n}', end = ' ')
        print(']')
    contador[2] += 1
    match input("Pressione qualquer tecla para voltar ao menu: "):
        case _:
            main()

    



def menu():
    print("MENU\n")
    print('1 - Intervalo\n2 - Intervalo Aberto e Fechado\n3 - Intervalo em ordem crescente ou decrescente\n0 - SAIR')
    escolha = input('Escolha: ')
    match escolha:
        case '1':
            intervalo()
        case '2':
            intervalo_aberto_fechado()
        case '3':
            intervalo_cres_decres()
        case '0':
            finalizar_programa()
        case _:
            limpa_tela()
            print("\nOPÇÃO INVÁLIDA")
            menu()
            



def main():
    limpa_tela()
    menu()


if __name__ == '__main__':
    main()