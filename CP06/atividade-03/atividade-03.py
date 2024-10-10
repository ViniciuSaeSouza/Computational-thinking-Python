#RM: 555678 --- NOME: João Victor Michaeli --- 1TDSPK
#RM: 554456 --- NOME: Vinicius Saes de Souza --- 1TDSPK
#RM: 558062 --- NOME: Henrique Francisco Garcia --- 1TDSPK

import oracledb
from datetime import datetime
import pandas as pd
import os

eleitor = {}

# SUB-ALGORITMOS

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input("\nPressione enter para continuar...")
    clear()

def verifica_chave(pk: str) ->  list[bool , pd.DataFrame]:
    lista_eleitores = []
    sql = f"SELECT * FROM urna WHERE cpf = '{pk}'"
    try:
        inst_select.execute(sql)
        result = inst_select.fetchall()
    except Exception as e:
        print(e)
        
    for dados in result:
        valores = {
            0 : 'cpf',
            1 : 'nome',
            2 : 'estado',
            3 : 'voto'
        }
        lista_eleitores.append(dados)
        for i, dado in enumerate(dados):
            if i != 4:
                eleitor[valores[i]] = dado
        
    data_frame = pd.DataFrame.from_records(lista_eleitores, columns=['CPF', 'Nome', 'Estado', 'Voto', 'Data'])
    if result:
        return True, data_frame
    else:
        return False, []
    
def cadastrar_voto() -> bool:
    clear()
    print('Cadastrando novo CPF\n')
    nome = input("Nome: ")
    estado = input("Estado: ")
    voto = input("Voto: ")
    sql_insert = f"INSERT INTO urna (CPF, NOME, ESTADO, VOTO, DATA_VOTO) VALUES (:1, :2, :3, :4, :5)"
    
    try:
        inst_insert.execute(sql_insert, (cpf, nome, estado, voto, datetime.now()))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def editar_voto(edicao: list[str], cpf: str):
    sql = f"UPDATE urna SET nome = '{edicao[0]}', estado = '{edicao[1]}', voto = '{edicao[2]}' WHERE cpf = '{cpf}'"
    try:
        inst_update.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def excluir_registro(cpf):
    sql = f"DELETE FROM urna WHERE cpf = '{cpf}'"
    
    try:
        inst_delete.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)

def listar_tudo():
    sql = f"SELECT * FROM urna"
    inst_select.execute(sql)
    data = inst_select.fetchall()
    data_frame = pd.DataFrame.from_records(data, columns=['CPF', 'Nome', 'Estado', 'Voto', 'Data'])

    if data_frame.empty:
        print('Não há nenhum cadastro registrado')
    else:
        print(data_frame)


try: 
    conn = oracledb.connect(user="RM555678", password="310302", dsn="oracle.fiap.com.br:1521/ORCL")
    inst_insert = conn.cursor()
    inst_select = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()
except Exception as e:
    print("Conexão deu erro: ", e)
    conexao = False
else:
    conexao = True


# Programa

clear()
while conexao:

    print("Bem-vindo ao sistema de votação!\n")
    cpf = input("Digite o Cpf ou 'L' para listar todos registros: ")
    
    if cpf.lower() == "l":
        clear()
        print("Registros salvos\n")
        listar_tudo()
        continuar()
    else:
        existe, data_frame = verifica_chave(cpf)
        if existe:
            clear()
            print("CPF já cadastrado, segue as informações\n")
            print(data_frame)
            escolha = input("\nDeseja Editar ou Excluir o registro? \n\n1 - Editar \n2 - Excluir \n\nEscolha: ")
            match escolha:
                case "1":
                    clear()
                    print(f"Editando dados do cpf: {cpf}\n")
                    novo_nome = input("Novo Nome: ") or eleitor['nome']
                    novo_estado = input("Novo Estado: ") or eleitor['estado']
                    novo_voto = input("Novo Voto: ") or eleitor['voto']
                    edicao = [novo_nome, novo_estado, novo_voto]
                    editar_voto(edicao, cpf)
                    print('\nCadastro editado com sucesso!')
                    continuar()
                case "2":
                    clear()
                    excluir_registro(cpf)
                    print('Registro excluido com sucesso!')
                    continuar()
                case _:
                    print("Opção inválida!")
        else:
            if cadastrar_voto():
                print("\nVoto cadastrado!")
                continuar()
            else:
                print("Deu xabu")