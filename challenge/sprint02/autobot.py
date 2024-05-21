import os
lista_numeros = '0123456789'

veiculos = []

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def tela_inicial():
    print(
"""
****************************
   BEM VINDO(A) AO AUTOBOT
   
****************************
"""
)
    
def menu_opcoes():
    print('1. Cadastrar Veículo')
    print('2. Painel de Problemas')
    print('3. Diário de Bordo')
    print('4. Consultar veículos')
    print('5. Sair do programa')
    nmrOpcoesMenu = 5
    escolhe_opcao(nmrOpcoesMenu)
    
def exibe_subtitulo(titulo: str):
    limpa_tela()
    titulo = titulo.upper()
    linha = '*' * (len(titulo) + 5)
    print(linha)
    # print(titulo.ljust(22)) # --------------------------- PQ NÃO DA O JUSTIFY????????????????
    print(titulo.center(len(linha)))
    print(linha)
    
def finaliza_programa():
    exibe_subtitulo('..Finalizando programa..')
    exit()

def eh_alphanumeric(s: str) -> bool:
        return s.isalnum()
    
def consultar_veiculos():
    print(veiculos)
    match int(input('1. Voltar ao menu principal\n2. Finalizar programa\nMenu: ')):
        case 1:
            main()
        case 2:
            finaliza_programa()
    
def cadastrar_veiculo():
    limpa_tela()
    exibe_subtitulo('cadastrar veiculo')
    atributos_carro = ['Fabricante', 'Modelo', 'Ano', 'Placa']
    
    for atributo in atributos_carro:
        s = input(f'{atributo}: ')
        while not eh_alphanumeric(s) or not s.strip():
            print(f"Erro! {atributo} do veículo não pode estar vazio(a) e não pode conter caracteres especiais (@*$-/...).")
            s = input(f'{atributo}: ')
        veiculos.append(f'{atributo.upper()}: {s.upper()}')
        
    print("\nVeículo cadastrado com sucesso!\nVerificar seus veículos?")
    match int(input('1. Sim\n2. Não\nMenu: ')):
        case 1:
            consultar_veiculos()
        case 2:
            main()
    print(veiculos)
        

def escolhe_opcao(nrItens):
    opcao = input('Menu: ')
    while True:
        if  not opcao.isdigit() or int(opcao) > nrItens or int(opcao) <= 0:
            print('Erro! Digite uma opção válida do menu.')
            opcao = input('Menu: ')
        else:
            opcao = int(opcao)
            break
    
    match opcao:
        case 1:
            cadastrar_veiculo()
        case 2:
            painel_de_problemas() # A FAZER
        case 3:
            diario_de_bordo() # A FAZER
        case 4:
            consultar_veiculos()
        case 5:
            finaliza_programa()
        case _:
            print("Erro! digite uma opção válida")
                
            
            
def main():
    limpa_tela()
    tela_inicial()
    menu_opcoes()
    escolhe_opcao(5)


if __name__ == '__main__':
    main()