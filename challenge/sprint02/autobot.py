import os
lista_numeros = '0123456789'

veiculos = []

def telaInicial():
    print(
"""
****************************
Bem-vindo(a) ao AutoBot!
****************************
"""
)
    
def menuOpcoes():
    print('1. Cadastrar Veículo')
    print('2. Painel de Problemas')
    print('3. Diário de Bordo')
    print('4. Consultar veículos')
    print('5. Sair do programa')
    nmrOpcoesMenu = 5
    escolheOpcao(nmrOpcoesMenu)
    
def exibeSubtitulo(titulo: str) -> str:
    linha = '*' * (len(titulo) + 5)
    print(linha)
    print(titulo.upper())
    print(linha)

def ehNumeroOuLetra(s: str) -> bool:
        return s.isalnum()    
    
def cadastrarVeiculo(titulo: str):
    os.system('cls')
    exibeSubtitulo(titulo)
    #------------------------------------------------------------------------- EMPAQUEI AQUI
    fabricante = s = input("Fabricante: ")
    modelo = s = input("Modelo: ")
    while not ehNumeroOuLetra(s) or not s.strip(): # como faço pra verificar cada input se é letra ou não
        print(f"Erro!  do veículo não pode estar vazio(a) e não pode conter caracteres especiais (@*$-/...).")
        s = input('Menu: ')
    veiculos.append(f': {s}')
    return s.upper()
        

def escolheOpcao(nrItens):
    opcao = input('Menu: ')
    while True:
        if  not opcao.isdigit() or int(opcao) > nrItens:
            print('Erro! Digite uma opção válida do menu.')
            opcao = input('Menu: ')
        else:
            opcao = int(opcao)
            break
    
    match opcao:
        case 1:
            cadastrarVeiculo('cadastrar veiculo')
        case 2:
            painelDeProblemas()
        case 3:
            diarioDeBordo()
        case 4:
            consultarVeiculo()
        case 5:
            os.system('cls')
        case _:
            print("Erro! digite uma opção válida")
                
            
            
def main():
    telaInicial()
    menuOpcoes()
    escolheOpcao()


if __name__ == '__main__':
    main()