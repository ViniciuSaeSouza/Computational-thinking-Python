import os
os.system("cls")

forma_pagamento = int(input("Forma de pagamento Digite - ""1"" p/ Crédito ou ""2"" p/ Outros: "))
# valor = 0
# valor_final = 0
acrescimo = 1.05
desconto = 0.95
acres_desc = acrescimo or desconto
desc_acre_txt = "acrescimo"

if    forma_pagamento != 1 and forma_pagamento != 2:
        print("""
        Desculpe, forma de pagemto inválida.
        Compra não realizada.""")    
else:
    if (forma_pagamento == 1):
        valor = float(input("Valor: ")) 
        forma_pagamento = "Crédito"
        valor_final = valor * acrescimo
        desc_acre_txt = "acrescimo"
    elif forma_pagamento == 2:
        valor = float(input("Valor: "))
        forma_pagamento = "Outros"
        valor_final = valor * desconto
        desc_acre_txt = "desconto"
    print(f"""
Forma de Pagamento.......: {forma_pagamento}
Valor da Compra..........: R$ {valor:10.2f}
Valor total com {desc_acre_txt} : R$ {valor_final: 10.2f}
"""
)