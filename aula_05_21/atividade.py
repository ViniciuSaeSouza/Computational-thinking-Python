# Vinicius Saes de Souza - RM 554456

# def isFloat(s: str) ->bool:
#     digito = '0123456789.'
#     valido = True
#     ponto = 0
#     if s[0] in '+-' or s[0] in digito:
#         for i in range(1, len(s)):
#             if s[i] == '.':
#                 ponto += 1
#                 if ponto > 1:
#                     valido = False
#                     break
#             if s[i] not in digito:
#                 valido = False
#                 break
#         else:
#             valido = True
#             return valido

# # ------------ Programa principal

# x = input('Digite um float: ')
# while True:
#     if not isFloat(x):
#         x = input("Erro\nDigite um Float: ")
#     else:
#         x = float(x)
#         print(f'Float digitado: {x}')
#         break


s = "1234-"

def ehAlphaNum(s:str) -> bool:
    return s.isalnum()

print(ehAlphaNum(s))