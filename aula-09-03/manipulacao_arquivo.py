# manipulação de arquivos
"""
Modo de abertura:
-------------------------------------
'w' | write - Gravação -> se existir o arquivo, ele sobregrava
'r' | read - Leitura
'a' | append - Edição
'x' | gravação em arquivo exclusivo
'+' | leitura e gravação

Função open() -> abre um arquivo
Função read() -> lê um arquivo
Função write() -> grava arquivo
--------------------------------------
Sintaxe:
  <obj> = open("nome_arquivo", "modo_abertura")
"""

# GRAVANDO EM UM ARQUIVO
"""
arquivo = open("1tdspk.txt", "w")
arquivo.write("Nossa que legal!\n")
arquivo.write("To manjando nada não, lá ele")
arquivo.close()

print("Arquivo gravado.")
"""
# Lendo um arquivo
"""
arquivo = open("1tdspk.txt","r")
print(arquivo.read())
arquivo.close()
"""

# Editando um arquivo, 'apendando'
"""arquivo = open("1tdspk.txt", "a", encoding='utf-8')
arquivo.write('\nAdicionei essa nova linha com o append, óia que legal')
arquivo.close()"""

# with - Operador de contexto (não necessita o `.close()`)
"""with open("1tdspk.txt", 'w+', encoding='utf-8') as arquivo:
  arquivo.write("Utilizando o operador de contexto 'with'")
  arquivo.write("\nUtilizando o operador de contexto 'with'")
  arquivo.write("\nUtilizando o operador de contexto 'with'")
  arquivo.seek(0) # seek posiciona o cursor no arquivo
  print(arquivo.read())"""
  
