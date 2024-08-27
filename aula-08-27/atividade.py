# Maria Eduarda Alves da Paixão - RM:558832

import os
os.system("cls")

#Exibe todos os itens do menu
def exibir_menu() -> None:
    print("""
MENU:

0 - SAIR
1 - Digite um nome completo
2 - Exibe separado o Nome do Sobrenome
3 - Conta quantas palavras há no nome completo
4 - Exibir em formato de bibliografia
          
""")
    
# Exibe uma mensagem formatada.
# Parâmetro 1: carac -> str: O caractere que formará a mensagem
# Parâmetro 2: msg -> str: A mensagem que será exibida
# Retorno: None
def mensagem(carac:str, msg: str) -> None:
    tamanho = len(msg)
    print(f"\n{carac * tamanho}")
    print(msg)
    print(f"{carac * tamanho}")

#Separa um nome completo por nome e sobrenome
#Parâmetro: n -> str: parâmetro que tem a String nome completa
#Retorno: None 
def separar_nome_sobrenome(n: str) -> None:
    lista_nome = n.split()

    print(f"Nome: {lista_nome[0]}")
    print(f"Sobrenome: {" ".join(lista_nome[1:len(lista_nome):1])}")
    
#Conta quantas palavras tem em uma String 
#Parâmetro: n -> str: parâmetro que tem a String nome completa
#Retorno: None 
def conta_palavras_nome(n: str)->None:
    lista_nome = n.split()
    print(f"O nome {n} tem {len(lista_nome)} ", end="")
    print("palavras.") if len(lista_nome) > 1 else print("palavra.")

#Formata um nome (String) no formato bibliografia. (Último sobrenome em maiúsculo, e o restante em seguindo o padrão.EX: Maria Paixao -> PAIXAO, Maria).
#Parâmetro: n -> str: parâmetro que tem a String nome completa.
#Retorno: None 
def formato_bibliografia(n: str) -> None:
    lista_nome = n.split()

    print(f"{lista_nome[-1].upper()}, {" ".join(lista_nome[0:-1:1])}")


nome = ""
msg_n_adicionado = "Primeiramente digite um nome na opção 1."

while True:
    os.system("cls")
    exibir_menu()
    opcao = input("Escolha: ")
    os.system("cls")

    match opcao:
        case "0":
            mensagem("!", "Agradecemos por usar nosso sistema!")
            break
        case "1":
            nome = input("Digite um nome completo: \n")
            
        case "2":
            if nome != "":
                separar_nome_sobrenome(nome)
            else:
                mensagem("-", msg_n_adicionado)  

        case "3":
            if nome != "":
                conta_palavras_nome(nome)
            else:
                mensagem("-", msg_n_adicionado)  
            
        case "4":
            if nome != "":
                formato_bibliografia(nome)
            else:
                mensagem("-", msg_n_adicionado)  

        case _: 
            mensagem("-", "Opção inválida, digite um item de 0 a 4")
            print()
    
    input("\nPressione alguma tecla para continuar...")
          