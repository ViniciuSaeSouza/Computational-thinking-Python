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
# Try catch para a escolha da opção do menu inicial
)
try:
    opcao_escolhida = int(input("Digite uma opção: ")) #input da opção do menu escolhida (deve ser int)
    match opcao_escolhida:
        case 1: #Cadastrar o veículo, colhendo input de Marca (não pode ser vazio), Ano de fabricação (deve ser entre 1930 até ano atual(2024) e tipo int) e Placa do veículo (será convertida para maiúsculo))
            marca_veiculo = input("Digite a marca do seu veículo: ")
            
            while marca_veiculo == "":
                print("Erro! Marca do veículo não pode estar vazia.")
                marca_veiculo = input("Digite a marca do seu veículo: ")
                
            ano_veiculo = int(input("Ano de fabricação: "))
            
            while ano_veiculo == "" or ano_veiculo < 1930 or ano_veiculo > 2024:
                print("ERRO. Digite um ano válido")
                ano_veiculo = int(input("Ano de fabricação: "))
                
            placa_veiculo = (input("Placa do veículo: ")).upper()
            
            print(marca_veiculo,ano_veiculo,placa_veiculo) #Mostra os dados coletados para verificação
        
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
        case _:
            print("Opção inválida! digite o número correspondente com a opção desejada.")
except:
    print("Opção inválida! digite o número correspondente com a opção desejada.")
    
