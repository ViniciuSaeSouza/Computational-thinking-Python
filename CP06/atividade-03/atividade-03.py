#RM: 555678 --- NOME: João Victor Michaeli --- 1TDSPK
#RM: 554456 --- NOME: Vinicius Saes de Souza --- 1TDSPK
#RM: 558062 --- NOME: Henrique Francisco Garcia --- 1TDSPK

import oracledb
import datetime
import pandas as pd
eleitor = {}
lista_eleitores = []
# SUB-ALGORITMOS
def verifica_chave(pk: str) ->  list[bool , pd.DataFrame]:
    sql = f"SELECT * FROM urna WHERE cpf = '{pk}'"
    inst_select.execute(sql)
    result = inst_select.fetchall()
    for dado in result:
        lista_eleitores.append(dado)
        
    data_frame = pd.DataFrame.from_records(lista_eleitores, columns=['cpf', 'nome', 'cidade', 'voto'])
    if result:
        return True, data_frame
    else:
        return False, []
            

try: 
    conn = oracledb.connect(user="RM555678", password="310302", dsn="oracle.fiap.com.br:1521/ORCL")
    # print('Conexão recuperada com sucesso!')
    inst_insert = conn.cursor()
    inst_select = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()
except Exception as e:
    print("Conexão deu erro: " + e) 
    conexao = False
else:
    conexao = True




while conexao:
    chave = input("Digite o CPF: ")
    existe, data_frame = verifica_chave(chave)
    # print(data_frame)
    
    for dado in data_frame:
        lista_eleitores[dado] = 
    if existe:
        print("-- registro encontrado -- ")
        print(data_frame)
        
        
    






chave = 123

verifica_chave(chave)

conn.close()
