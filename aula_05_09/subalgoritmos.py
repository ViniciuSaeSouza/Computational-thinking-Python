def saudacao(usuario: str = "Edson", hora: int = 8) -> None:
    if hora < 12:
        turno = "Bom dia"
    elif hora <18:
        turno = "Boa tarde"
    else:
        turno = "Boa noite"
    print(f"{usuario}, {turno}! Seja bem vindo(a) á Fiap")

import os
os.system('cls')
# totalmente default
saudacao()
# parcialmente default
saudacao("Maria")
#parcialmente default
saudacao(hora = 13)