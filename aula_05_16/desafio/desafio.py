# # 4. Sabemos que o método isdigit() e/ou isnumeric() analisam uma string passado por parâmetro e retorna true caso tenha somente números ou false caso um dos caracteres não seja Numerico.

# x = "123"
# print(x.isdigit())
# # True

# x = "A123"
# print(x.isdigit())
# # False

# # Porém a falha deste método é a de retornar false caso algum texto com numero inicie com + ou -.
# x = '-453'
# print(x.isdigit())
# # False
# -----------------------------------------------------------
# def eh_numero(n:str) -> bool:
#     operadores = '+-'
#     proibidos = ',.abcdefghijklmnopqrstuvwxyz'
#     resultado = bool
#     for i in range(len(n)):
#         if n[0] in operadores:
#             resultado = True
#         elif n[0] in proibidos:
#             resultado = False
#         for o in range(1, len(n),1):
#             if n[o] in proibidos or n[o] in operadores:
#                 resultado = False
#     return resultado

def eh_numero (n:str) -> bool:
    operadores = '+-'
    numeros = '0123456789'
    resultado = bool
    if n[0] in operadores or n[0] in numeros:
        resultado = True
    else:
        resultado = False
    for i in range (1, len(n),1):
            if n[i] in numeros:
                resultado = True
            else:
                return False
                break
    return resultado

inteiro = input("Número: ")

print(f"{inteiro} é número inteiro =  {eh_numero(inteiro)}")
#True