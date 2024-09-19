"""
SINTAXE:
[<variavel>] = [<comando True>] if [<condicao>] else [<comando False>]
"""

# Sem usar variável
import os
os.system('cls' if os.name == 'nt' else 'clear')
idade = 17
print("Maior de idade") if idade > 18 else print("De Menó")


"""
SINTAXE:
[<variavel>] = [<comando True>] if [<condicao>] else [<comando False>]
"""

venda = 5000
bonus = 50 if venda > 1000 else 30
print(bonus)



"""
SINTAXE:
[<variavel>] = [<comando True>] if [<condicao>] else [<comando False>]
"""

venda = 1000
desconto = venda - (venda * 0.1 if venda > 1000 else venda * 0.05)

print(desconto)
print(venda)