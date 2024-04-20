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
3 - Consultar preço de peças
"""
)
try:
    opcao_escolhida = int(input("Digite uma opção: "))
    match opcao_escolhida:
        case 1:
            marca_veiculo = input("Digite a marca do seu veículo: ")
            ano_veiculo = int(input("Ano de fabricação: "))
            placa_veiculo = (input("Placa do veículo: ") )
except:
    print("Opção inválida! digite o número correspondente com a opção desejada.")