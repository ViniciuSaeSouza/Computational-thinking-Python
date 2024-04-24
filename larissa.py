import os
os.system('cls')

# Pega o valor da compra digitado pelo usuário
valor_compra = float(input("Valor da compra: "))

# Pergunta se o usuário quer utilizar o cumpom ou não (1 = sim / 2 = não)
usa_cupom = input("Utilizar cupom? 1 - Sim || 2 - Não: ")

if usa_cupom == "1": # Se o usuário digita "1" começa a verificar o valor da compra
    if valor_compra > 20: # SE o valor_compra for maior que 20, aplica o desconto e mostra na tela(print()) o valor final
        valor_final = valor_compra - 20
        print(f"Valor final da compra com cupom: R$ {valor_final:.2f}")
    else: # SE o valor_compra for menor que 20, NÃO aplica o desconto e mostra na tela(print()) o valor final e a mensagem de erro
        print("Valor da compra está abaixo do valor do desconto! Cupom não foi utilizado")
        print(f"Valor da compra sem cupom: R$ {valor_compra:.2f}")
elif usa_cupom == "2": # SE o usuário digita "2", não verifica nada e apenas mostra o valor da compra na tela
    print(f"Valor da compra: R$ {valor_compra:.2f}")
else:
    print("Erro, digite 1 para usar o cupom ou 2 para não utilizar o cupom.") # Caso o usuário não digite "1" ou "2", mostra mensagem de erro.
