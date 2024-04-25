import os
os.system('cls')

# Tela inicial com opções
print(
"""
****************************
  Bem-vindo(a) ao AutoBot!
****************************

1 - Cadastrar Veículo
2 - Painel de problemas
3 - Diário de Bordo
4 - Sair do programa
"""
)

# Try catch para a escolha da opção do menu inicial
try:
    opcao_escolhida = int(input("Digite uma opção: ")) #input da opção do menu escolhida (deve ser int)
    match opcao_escolhida:
        case 1: #Cadastrar o veículo, colhendo input de Marca (não pode ser vazio), Modelo do Veículo (não pode ser vazio), Ano de fabricação (deve ser entre 1930 até ano atual(2024) e tipo int) e Placa do veículo (será convertida para maiúsculo))
            fabricante_veiculo = input("Digite a fabricante do seu veículo: ")
            
            while fabricante_veiculo == "":
                print("Erro! Marca do veículo não pode estar vazia.")
                fabricante_veiculo = input("Digite a marca do seu veículo: ")
                
            modelo_veiculo = input("Digite o modelo do seu veículo: ")
            
            while modelo_veiculo == "":
                print("Erro! Marca do veículo não pode estar vazia.")
                modelo_veiculo = input("Digite a modelo do seu veículo: ")
                
            ano_veiculo = int(input("Ano de fabricação: "))
            
            while ano_veiculo == "" or ano_veiculo < 1930 or ano_veiculo > 2024:
                print("ERRO. Digite um ano válido")
                ano_veiculo = int(input("Ano de fabricação: "))
                
            placa_veiculo = input("Placa do veículo: ").upper()
            
            while placa_veiculo == "":
                print(f"ERRO. Placa {placa_veiculo} digitada é inválida. Digite novamente.")
                placa_veiculo = input("Placa do veículo: ").upper()
            
            os.system('cls')
            print(f'{fabricante_veiculo} || {modelo_veiculo} || {ano_veiculo} || {placa_veiculo}') #Mostra os dados coletados para verificação
        
        case 2: # Lista opções de problemas comuns automotivos, usuário escolhe a opção com números e recebe uma descrição do problema
            try:
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
            except:
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
except:
    os.system('cls')
    print("Opção inválida! digite o número correspondente com a opção desejada.")
    
