# caminho = "c:\\Users\\labsfiap\\Desktop\\Computational-thinking-Python\\aula-09-05" #Windows
# caminho = "c:/Users/labsfiap/Desktop/Computational-thinking-Python/aula-09-05" #Mac Linux

#Lendo um trecho de arquivo
# with open("arq.txt", "w+", encoding="utf-8") as arq:
#     arq.write("Desejo um bom dia\n")
#     arq.write("Não desejo mais nada\n")
#     arq.seek() # Posiciona o cursor na posição do elemento passado por parâmetro
#     print(arq.read(10))

documento = []

with open("arq.txt", "w+", encoding="utf-8") as arq:
    
    # Exibindo a gravação das linhas do arquivo
    print("\nExibindo a gravação linha linha...")
    arq.write("Linha1\n")    
    arq.write("Linha2\n")    
    arq.write("Linha3\n")    
    arq.seek(0)
    documento = arq.readlines()
    for i, linha in enumerate(documento):
        print(f"{i} -> {linha}", end="")
    print(documento)


    # Gravando varias linhas de uma vez
    """documento = []
    while True:
        linha = input("Linha: ")
        if linha != "":
            documento.append(linha + '\n')
        else:
            break
    arq.writelines(documento)
    arq.close()"""

    # Gravando linha a linha
    """    
    print("Gravando uma linha por vez...")
    while True:
        linha = input("Linha: ")
        if linha != "":
            arq.write(linha + "\n")
        else:
            break
    print("Exibindo a gravação...")
    arq.seek(0)
    print(arq.read())
    """
    
    # Método readlines()
    """arq.write("Primeira linha \n")
    arq.write("Segunda linha \n")
    arq.write("Terceira linha \n")
    arq.seek(0)
    arq.readlines()
    arq.seek(0)
    print("----------------------")
    for i, linha in enumerate(arq.readlines()):
        print(f"{i} -> {linha}.????()")"""

    #Utilizando o metodo readlines() - Lê apenas uma linha
    """
    arq.write("Primeira linha \n")
    arq.write("Segunda linha \n")
    arq.write("Terceira linha \n")
    arq.seek(1)
    print(arq.readline())"""
