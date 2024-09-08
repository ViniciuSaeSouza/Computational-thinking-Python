# Vinicius Saes de Souza - RM 554456
# Anderson de Sousa Pedro - RM 552007

# Descrição do exercício;
"""
# Tendo uma lista de comentários, qual a palavra com mais ocorrência?
# gravar em uma lista ✔️
# gravar a lista em um arquivo sujo ✔️
# criar uma lista de string desse arquivo sujo ✔️
# transforma a lista de string em apenas uma string ✔️
# retirar todas as palavras e caracteres não relevantes ✔️
# criar uma lista de string com as palavras ✔️
# fazer um set das palavras e jogar em uma lista as palavras exclusivas ✔️
# pesquisar (contagem) as palavras exclusivas na lista com todas as palavras (use um dicionario ou uma nova lista para acumular as ocorrencias) ✔️
# grave em um arquivo limpo todas as palavras, inclusive as repetidas ✔️
"""
# Lista de preposições, artigos, pronomes, conjunções, verbos auxiliares;
stopwords = [
  'a', 'à', 'ao', 'aos', 'as', 'até', 'afim', 'ainda', 'além', 'antes', 'ao', 'aquela', 'aquelas',
  'aquele', 'aqueles', 'aquilo', 'as', 'atrás', 'após', 'bastante', 'bem', 'com', 'como', 'contra',
  'da', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'desde', 'dessa', 'dessas', 'desse', 'desses',
  'desta', 'destas', 'deste', 'destes', 'disso', 'disto', 'do', 'dos', 'e', 'ela', 'elas', 'ele', 'eles',
  'em', 'enquanto', 'entre', 'era', 'essa', 'essas', 'esse', 'esses', 'esta', 'estas', 'está', 'estão',
  'este', 'estes', 'eu', 'foi', 'fomos', 'foram', 'há', 'isso', 'isto', 'já', 'lhe', 'lhes', 'lá', 'mais',
  'mas', 'me', 'mesma', 'mesmas', 'mesmo', 'mesmos', 'minha', 'minhas', 'muito', 'na', 'nas', 'nem',
  'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'o', 'os', 'ou', 'para', 'pela',
  'pelas', 'pelo', 'pelos', 'por', 'qual', 'quando', 'que', 'quem', 'se', 'sem', 'sendo', 'será', 'seu',
  'seus', 'só', 'sobre', 'sua', 'suas', 'também', 'te', 'tem', 'tendo', 'tenho', 'teu', 'teus', 'tive',
  'tivemos', 'tiveram', 'tua', 'tuas', 'um', 'uma', 'umas', 'uns', 'vai', 'vão', 'você', 'vocês', 'vos',
  'à', 'às', 'é', 'ao', 'dos', 'pelos', 'pela', 'pelos'
]
# Lista de pontuações;
pontuacao = ['.', ',', ';', ':', '!', '?', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
# Lista juntando todos os itens a serem removidos ;
filtro_string = stopwords + pontuacao
# Comentários utilizando preposições, artigos e pontuação;
comentarios = [
  "Eu adoro pão de batata!",
  "Pão de batata é muito bom.",
  "Todo dia de manhã eu asso uma fornada de pão de batata.",
  "Para mim, pão de batata é a solução."
]
# Lista de strings lidas do arquivo_sujo.txt;

# Função que recebe uma lista de string e altera todas as ocorrências de quebra de linha <\n> por uma string vazia <""> ;
# EX:  
# input = ["str1\n", "str2\n", "str3\n"]
# output = ["str1", "str2", "str3"]
def remove_quebra_linha(lista:list[str]) -> list[str]:
  aux = []
  for s in lista:
    #s = s.removesuffix("\n")
    s = s.replace("\n","")
    aux.append(s)
  return aux

# Função que recebe uma lista de string e remove pontuações e stopwords, retornando uma string única;
# EX:  
# input = ["Olá, mundo!", "Eu amo Python."]
# output = "olá mundo eu amo python"
def tratamento_string(lista:list) -> str:
  string_completa_filtrada = ""
  for s in lista:
    for char in s:
      if char in pontuacao:
        s = s.replace(char, "")
    string_completa_filtrada += (s + " ")
  
  for word in stopwords:
    # word = " {} ".format(word)
    word = f" {word} "
    if word in string_completa_filtrada:
      string_completa_filtrada = string_completa_filtrada.replace(word, " ")
  return string_completa_filtrada

# Função que recebe uma string e retorna uma lista de palavras;
# EX:  
# input = "Olá, mundo! Eu amo Python."
# output = ["olá", "mundo", "eu", "amo", "python"]
def cria_lista_de_string(string:str) -> list[str]:
  lista = []
  aux = ""
  for char in string:
    char = char.lower()
    if char != " ":
      aux += char
    else:
      lista.append(aux)
      aux = ""
  return lista

# Função que recebe uma lista de palavras e retorna um dicionário com as palavras como chaves e valor 0;
# EX:  
# input = ["olá", "mundo", "eu", "amo", "python"]
# output = {"olá": 0, "mundo": 0, "eu": 0, "amo": 0, "python": 0}
def cria_dict_ocorrencia(lista:list) -> dict:
  aux = {}
  for palavra in lista:
    aux[palavra] = 0
  return aux

# Função que recebe uma lista de palavras e um dicionário, e retorna o dicionário com a contagem de ocorrências de cada palavra;
# EX:  
# input = ["olá", "mundo", "eu", "amo", "python", "olá", "mundo"]
# output = {"olá": 2, "mundo": 2, "eu": 1, "amo": 1, "python": 1}
def conta_ocorrencias (lista:list[str], dicionario:dict) -> dict:
  for palavra in lista:
    if palavra in dicionario:
      dicionario[palavra] += 1
  return dicionario
  
# Lê os comentários do usuário e grava em um arquivo chamado "arquivo_sujo.txt"
with open("arquivo_sujo.txt", "w+", encoding="utf-8") as arquivo_sujo:
  while True:
    comentario = input("Comentário: ")
    if comentario != "":
      comentarios.append(comentario)
    else:
      break
  arquivo_sujo.writelines("\n".join(comentarios))
  arquivo_sujo.seek(0)
  
  # Lê todas as linhas do <arquivo_sujo.txt>, remove as ocorrências de quebra de linha (<\n>) e atribui cada linha lida do arquivo como um elemento da lista_arquivo_sujo;
  lista_arquivo_sujo = remove_quebra_linha(arquivo_sujo.readlines())
  

# Itera os elementos da lista 'lista_arquivo_sujo' e cria uma string única sem pontuação e stopwords
string_completa_filtrada = tratamento_string(lista_arquivo_sujo)
# Adiciona cada palavra da 'string_completa_filtrada' como um elemento na 'lista_filtrada'
lista_palavras_filtradas = cria_lista_de_string(string_completa_filtrada)
# Cria um set que remove todas as palavras duplicadas
set_palavras_unicas = set(lista_palavras_filtradas)
# Cria um dicionário que define cada palavra do 'set_palavras_unicas' como chave e define um valo de '0'
dict_de_palavras_unicas = cria_dict_ocorrencia(set_palavras_unicas)
# Adiciona +1 ao valor de cada chave do 'dict_de_palavras_unicas' para contar quantas vezes cada palavra aparece
palavras_unicas_contadas = conta_ocorrencias(lista_palavras_filtradas , dict_de_palavras_unicas)

# Cria e escreve em um arquivo chamado 'arquivo_limpo.txt' todas as palavras (sem pontuação ou stopwords) mesmo que repetidas dentro de 'lista_palavras_filtradas'
with open("arquivo_limpo.txt", 'w+', encoding='utf-8') as arquivo_limpo:    
  arquivo_limpo.writelines("\n".join(lista_palavras_filtradas))
  

  
  


  
  
