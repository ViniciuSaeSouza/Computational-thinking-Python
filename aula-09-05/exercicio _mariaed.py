import os
os.system("cls")

#Tendo uma lista de comentários, qual a palavra com mais ocorrência?

lista_comentarios = [
    "esse tênis é muito fiel ao aúncio",
    "muito lindo, gostei",
    "feio, não gostei da qualidade",
    "pessímo!",
    "lindo!",
    "horrível",
    "não indico",
    "gostei do tênis, chegou rápido",
    "Esta qualidade é ruim, eu esperava mais desse tenis e do fabricante", 
    "Obrigada pelo atendimento, muito bom mesmo e o tênis é fiel a realidade"
]

# with open("arq_sujo.txt")
# arq_sujo = 

# gravar em uma lista
# gravar a lista em um arquivo sujo
# criar uma lista de string desse arquivo sujo
# transforma a lista de string em apenas uma string 
# retirar todas as palavras e caracteres não relevantes
# criar uma lista de string com as palavras 
# fazer um set das palavras e jogar em uma lista as palavras exclusivas
# pesquisar (contagem) as palavras exclusivas na lista com todas as palavras (use um dicionario ou uma nova lista para acumular as ocorrencias)
# grave em um arquivo limpo todas as palavras, inclusive as repetidas



# ------------------------------------------------

# caminho = "~\\Computational-thinking-Python\\aula-09-05"

# Descrição do exercício
"""
# Tendo uma lista de comentários, qual a palavra com mais ocorrência?
# gravar em uma lista
# gravar a lista em um arquivo sujo
# criar uma lista de string desse arquivo sujo
# transforma a lista de string em apenas uma string 
# retirar todas as palavras e caracteres não relevantes
# criar uma lista de string com as palavras 
# fazer um set das palavras e jogar em uma lista as palavras exclusivas
# pesquisar (contagem) as palavras exclusivas na lista com todas as palavras (use um dicionario ou uma nova lista para acumular as ocorrencias)
# grave em um arquivo limpo todas as palavras, inclusive as repetidas
"""
# Lista de preposições, artigos, pronomes, conjunções, verbos auxiliares
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
# Lista de pontuações
pontuacao = ['.', ',', ';', ':', '!', '?', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
# Lista juntando todos os itens a serem removidos 
lista_filtro = stopwords + pontuacao



# Comentários utilizando preposições, artigos e pontuação.
comentarios = [
  "Eu adoro pão de batata!",
  "Pão de batata é muito bom.",
  "Todo dia de manhã eu asso uma fornada de pão de batata.",
  "Para mim, pão de batata é a solução."
]

# Lista de strings lidas do arquivo_sujo.txt
lista_arquivo_sujo = []

def tratamento_strings(lista:list[str]) -> list[str]:
  aux = []
  for s in lista:
    #s = s.removesuffix("\n")
    s = s.replace("\n","")
    aux.append(s)
  return aux

with open("arquivo_sujo.txt", "w+", encoding="utf-8") as arquivo_sujo:
  while True:
    comentario = input("Comentário: ")
    if comentario != "":
      comentarios.append(comentario)
    else:
      break
  arquivo_sujo.writelines("\n".join(comentarios))
  arquivo_sujo.seek(0)
  lista_arquivo_sujo = tratamento_strings(arquivo_sujo.readlines())
  print(lista_arquivo_sujo)