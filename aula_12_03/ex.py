# Edson de Oliveira
# Estamos em uma black friday, há desconto para todo mundo :,). Quem efetuar uma compra até 1000 reais ganhará 100 de cashback, para os demais 200 de cashback. Fazer um algoritmo que exiba o valor original, o valor do cacshback ganho e o desconto com o cacsh back

# valor_compra = int(input("Digite o valor da sua compra: "))

# if valor_compra <= 1000 and valor_compra > 100:
#     cashback = 100
    
# else:
#     cashback = 200
    
# valor_final = valor_compra - cashback
# print(f"Valor da compra: {valor_compra}, CashBack: {cashback}, Valor final: {valor_final} ")


# Exercicio 2:
# Uma compra efetuada pelo usuário poderá ter desconto ou acréscimo.
# Se a compra for paga com cartão de crédito, será acrescido 2% no valor da compra
# Qualquer outro meio de pagamento haverá deconto de 5%.

valor_da_compra = float(input("Digite o valor da compra: "))
meio_de_pagamento = input("Pagamento: 1- cartão / 2- outros ")

if meio_de_pagamento == "1":
    modificador = 0.02
    modificador_texto = "juros"
    valor_final = valor_da_compra + (valor_da_compra * modificador)
else:
    modificador = 0.05
    modificador_texto = "desconto"
    valor_final = valor_da_compra + (valor_da_compra * modificador)
print(f"""
      O valor da sua compra é de: {valor_da_compra}
      O Valor do {modificador_texto} é de: {modificador * 100}%
      O valor final é: {valor_final}
      """)

    