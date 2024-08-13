# ================= DEFINIÇÃO DOS SUBALGORITMOS

# Definição da estrutura do dicionário
notas = {'Joao' :  9.5,
         'Maria': 10.0,
         'Jose' : 4.5}

# Rotina de cadastro de Aluno | Nota
def cadastrar_aluno():
    mensagem_titulo("Cadastrando Aluno")
    if len(notas) <= 10:
        nome = input("Nome: ")
        if nome == "":
            mensagem("!", "Proibido nome em branco!")
        else:
            if notas.get(nome) != None:
                mensagem('!', f"Ja existe o aluno {nome}")
            else:
                nota = input("Nota: ") # "22"
                if nota_valida(nota): # "34.6.4"
                    notas[nome] = float(nota)
                    mensagem("*", "Aluno cadastrado com sucesso!")
                else:
                    mensagem("!", f"A nota {nota} é inválida!")
    else:
        mensagem("!","A turma está lotada com 10 alunos!")
    input(msg_continuar)

# Rotina de Edição de Aluno | Nota
def editar_aluno():
    mensagem_titulo("Editando um Aluno")
    nome = input("Nome: ")
    if not notas.get(nome):
        mensagem("!", f"O aluno {nome} não existe!")
    else:
        print(f"Nota anterior {notas[nome]}")
        nota = input("Nova Nota: ")
        if nota_valida(nota):
            notas[nome] = float(nota)
            mensagem("!","Dados atualizados com sucesso!")
        else:
            mensagem("!",f"Nota inválida!")
    input(msg_continuar)

# Rotina de Listagem de Aluno | Nota
def listar_alunos():
    mensagem_titulo("Listagem dos alunos")
    print("\nNOME           NOTA")
    print("-------------------")
    for nome, nota in notas.items():
        espaco = 15 - len(nome) # 15 - 5 = 10
        print(f"{nome}{espaco * ' '}{nota:4.1f}") # '10.0'

    input(msg_continuar) # input manco

# Rotina de Exclusão de Aluno | Nota
def excluir_aluno():
    mensagem_titulo("Excluindo um aluno")
    nome = input("\nNome: ")
    if not notas.get(nome) :
        mensagem("!",f"O aluno {nome} não existe!")
    else:
        del notas[nome]
        mensagem("!","Aluno removido!")
    input(msg_continuar)

# Rotina de Cálculo da média da turma
def calcular_media():
    mensagem_titulo("Calculando a média da turma")
    soma = 0
    # soma as notas gravadas
    for nota in notas.values():
        soma += nota
    # Calcula a média
    media = soma / len(notas)
    mensagem("-",f"Média dos {len(notas)} alunos => {media:.1f}")
    input(msg_continuar)

# Rotina de consulta de Aluno | Nota
def consultar_aluno():
    mensagem_titulo("\nConsultando um aluno")
    nome = input("\nNome: ")

    if notas.get(nome):
        nota = notas[nome]
        print("\nNOME           NOTA")
        espaco = 15 - len(nome)
        mensagem("-",f"{nome}{espaco*' '}{nota:4.1f}")
    else:
        mensagem("!",f"O aluno {nome} não existe!")
    input(msg_continuar)

# Verifica se uma string 'v' é float.
# Parâmetro: v -> str
# Retorno: bool
def isfloat(v: str) -> bool: # "346.4"
    valor_aux = v.replace('.','',1) # substitua o primeiro ponto por vazio # "346.4" 
    return valor_aux.isdigit() # "346.4" False

# Verifica se um valor 'n' corresponde a uma nota.
# Parâmetro: n -> float
# Retorno: bool
def isValida(n: float) -> bool: # 22
    return n >= 0 and n <= 10 # False

# Verifica se um valor 'n' corresponde a uma nota, valor float válido.
# Parâmetro: n -> str
# Retorno: bool
def nota_valida(n: str) -> bool: # "34.6.4"
    if isfloat(n): # "34.6.4"
        n = float(n) # "22" -> 22
        if isValida(n): # 22
            return True
        else:
            return False

# Exibe uma mensagem formatada.
# Parâmetro 1: carac -> str: O caractere que formará a mensagem
# Parâmetro 2: msg -> str: A mensagem que será exibida
# Retorno: None
def mensagem(carac:str, msg: str) -> None:
    tamanho = len(msg)
    print(f"\n{carac * tamanho}")
    print(msg)
    print(f"{carac * tamanho}")

# Formata a mensagem de título.
# Parâmetro: msg -> str: A mensagem que será exibida no título
# Retorno: None
def mensagem_titulo(msg: str) -> None:
    tamanho = len(msg)
    print(f"\n{msg}\n{tamanho * '='}")

# Exibição do menu
def exibe_menu() -> None:
    print("""
    0 - SAIR
    1 - Adicionar novo Aluno | Nota (limite 10 alunos)
    2 - Editar Aluno | Nota
    3 - Listar os Alunos
    4 - Excluir um Aluno
    5 - Calcular a média da turma
    6 - Consultar um aluno
    7 - Apagar todos os alunos da sala    
    """)

# ================= PROGRAMA PRINCIPAL
import os

msg_continuar = "\nPressione alguma tecla para continuar . . ."

while True:
    os.system("clear")
 
    exibe_menu()
    escolha = input("Escolha: ")
    os.system("clear")
    match  escolha:
        case '0': 
            break 
        case '1':
            cadastrar_aluno()
        case '2':
            editar_aluno()
        case '3':
            listar_alunos()
        case '4':
            excluir_aluno()            
        case '5':
            calcular_media()
            
        case '6':
            consultar_aluno()
        case '7':
            mensagem_titulo("APAGANDO TODOS OS ALUNOS DA TURMA")
            resp = input("\nConfirma a exclusão da turma? <S>im ou <N>ão: ")
            if resp.upper() == "S":
                del notas
                mensagem("!","TURMA EXCLUÍDA!")
                notas = dict()
            else:
                mensagem("-","Exclusão cancelada!")
            input(msg_continuar)
        case '8':
            mensagem_titulo("Olha que legal este baguio")
            input(msg_continuar)
        case _:
            mensagem("*","OPÇÃO INVÁLIDA!")
            input(msg_continuar)
                
