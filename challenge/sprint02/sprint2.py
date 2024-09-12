import os
os.system('cls')

veiculos = []

lista_numeros = ['0123456789']
lista_letras = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

# Tela inicial com titulo do programa **********************
def tituloInicial():
    print(
"""
****************************
Bem-vindo(a) ao AutoBot!
****************************
"""
)

# Exibe as opções do painel inicial ************************
def exibirOpcoes():
    print("1 - Cadastrar Veículo")
    print("\n2 - Painel de problemas")
    print("\n3 - Diário de Bordo")
    print("\n4 - Sair do programa")
    
# Exibe subtitulo do menu de cada funcionalidade ************************
def exibirSubtitulo(texto):
    os.system('cls')
    linha = ('*' * (len(texto)+ 5))
    print(f'{linha}')
    print(texto)
    print(f'{linha}\n')
    
def infoValida(texto:str, info:str) -> str:
    texto_formatado = texto.capitalize()

    def ehLetraOuNumero(info: str) -> bool:
        return info.isalpha() or info.isdigit()

    if texto == 'ano':
        while not info.isdigit() or not info.strip():
            print(f"Erro! {texto_formatado} do veículo não pode estar vazio(a), não pode conter letras ou caracteres especiais (@*$-/...).")
            info = input(f"{texto_formatado} do seu veículo: ")
        return info
    
    # ------------------ EMPAQUEI AQUI, FUNÇÃO 'ehLetraOuNumero' NÃO ESTÁ SENDO CHAMADA
    
    while not info.strip() or not ehLetraOuNumero(info):
        print(f"Erro! {texto_formatado} do veículo não pode estar vazio(a) e não pode conter caracteres especiais (@*$...).")
        info = input(f"{texto_formatado} do seu veículo: ")
    return info


#Cadastrar o veículo, colhendo input de Marca (não pode ser vazio), Modelo do Veículo (não pode ser vazio), Ano de fabricação (deve ser entre 1930 até ano atual(2024) e tipo int) e Placa do veículo (será convertida para maiúsculo))
def cadastrarVeiculo():
    exibirSubtitulo('Cadastro de novo Veículo')
    
    fabricante_veiculo = infoValida("fabricante", input("Digite a fabricante do seu veículo: ").upper())
        
    modelo_veiculo = infoValida('modelo',input("Digite o modelo do seu veículo: ").upper())
    # while modelo_veiculo == "":
    #     print("Erro! Marca do veículo não pode estar vazia.")
    #     modelo_veiculo = input("Digite a modelo do seu veículo: ").upper()
        
    ano_veiculo = infoValida('ano',input("Ano de fabricação: "))
    # while ano_veiculo == "" or ano_veiculo < 1930 or ano_veiculo > 2024:
    #     print("ERRO. Digite um ano válido")
    # ano_veiculo = input("Ano de fabricação: ")
        
    placa_veiculo = infoValida('placa',input("Placa do veículo: ").upper())
    # while placa_veiculo == "":
    #     print(f"ERRO. Placa {placa_veiculo} digitada é inválida. Digite novamente.")
    #     placa_veiculo = int(input("Placa do veículo: ")).upper()
    
    os.system('cls')
    veiculos.append([fabricante_veiculo, modelo_veiculo, ano_veiculo, placa_veiculo])
    print(f'Veículo cadastrado! \nFabricante: {fabricante_veiculo} || Modelo: {modelo_veiculo} || Ano: {ano_veiculo} || Placa: {placa_veiculo}') #Mostra os dados coletados para verificação
    
    # Debug
    print(veiculos)
    
def escolherOpcao():
    # Match case para a escolha da opção do menu inicial
    opcao_escolhida = int(input("Digite uma opção: ")) #input da opção do menu escolhida (deve ser int)
    match opcao_escolhida:
        case 1: 
            cadastrarVeiculo()
        
        case 2: # Lista opções de problemas comuns automotivos, usuário escolhe a opção com números e recebe uma descrição do problema
            
            problema_painel_escolhido = int(input("""
    1 - Óleo
    2 - Bateria
    3 - Radiador
    Opção: """))
            match problema_painel_escolhido: #Identifica a opção escolhida e retorna a descrição correspondente // COMO FAZER O PROGRAMA RETORNAR PARA MENU DE ESCOLHA
                case 1:
                    print("Descrição de problemas e soluções relacionadas ao óleo")
                case 2:
                    print("Descrição de problemas e soluções relacionadas a bateria")
                case 3:
                    print("Descrição de problemas e soluções relacionadas ao radiador")
                case _:
                    print("Opção inválida! digite o número correspondente com a opção desejada.")
                
        case 3:
            check_pneu = input("Checou o estado do Pneu? S/N: ").upper()
            while check_pneu != "S" and check_pneu != "N":
                print(f"ERRO! Tecla '{check_pneu}' inválida. Digite S ou N")
                check_pneu = input("Checou o estado do Pneu? S/N: ").upper()
            
            check_calibrar = input("Calibrou o Pneu? S/N: ").upper()
            while check_calibrar != "S" and check_calibrar != "N":
                print(f"ERRO! Tecla '{check_calibrar}' inválida. Digite S ou N")
                check_calibrar = input("Checou o estado do Pneu? S/N: ").upper()
                
            check_oleo = input("Checou o nível do Óleo? S/N: ").upper()
            while check_oleo != "S" and check_oleo != "N":
                print(f"ERRO! Tecla '{check_oleo}' inválida. Digite S ou N")
                check_oleo = input("Checou o estado do Pneu? S/N: ").upper()
                
            check_farois = input("Checou as Luzes do carro? S/N: ").upper()
            while check_farois != "S" and check_farois != "N":
                print(f"ERRO! Tecla '{check_farois}' inválida. Digite S ou N")
                check_farois = input("Checou o estado do Pneu? S/N: ").upper()
                
            os.system('cls')
            print(f"""
    CheckList Diário de Bordo:

    Pneu checado:...................... {check_pneu}
    Pneu calibrado:.................... {check_calibrar}
    Checou o óleo:..................... {check_oleo}
    Checou as luzes:................... {check_farois}
    """)
        case 4:
            os.system('cls')
        case _:
            os.system('cls')
            print("Opção inválida! digite o número correspondente com a opção desejada.")

def main():
    os.system('cls')
    tituloInicial()
    exibirOpcoes()
    escolherOpcao()


if __name__ == '__main__':
    main()
    
