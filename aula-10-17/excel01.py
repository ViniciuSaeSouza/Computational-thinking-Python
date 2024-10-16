import os
import oracledb
import pandas as pd
from datetime import datetime


try:
    conn = oracledb.connect(user="RM554456", password="080995", dsn="oracle.fiap.com.br:1521/ORCL")
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as e:
    conexao = False
else:
    conexao = True
    ano_mes_dia = str(datetime.now().date())
    ano_mes_dia = ano_mes_dia.replace("-", "")
    hora = str(datetime.now().hour) + (str)(datetime.now().minute) + (str)(datetime.now().second)
    dia_hora = ano_mes_dia + hora
    

# Criação da tablea
inst_cadastro.execute("DROP TABLE petshop")
inst_cadastro.execute("CREATE TABLE petshop (id INTEGER GENERATED BY DEFAULT AS IDENTITY, tipo_pet VARCHAR(30), nome_pet VARCHAR(50), idade NUMBER)")

    
while conexao:
    # os.system('cls')
    print("""
0 - Sair
1 - Cadastrar
2 - Listar / exportar
""")
    inst_consulta.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'PETSHOP'")
    print(inst_consulta.fetchall())
    escolha = int(input("Escolha: "))
    
    match escolha:
        case 0:
            conexao = False
        case 1:
            tipo = input("Tipo...: ")
            nome = input("Nome...: ")
            idade = int(input("Idade...: "))
            cadastro = f"""INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES ('{tipo}', '{nome}', '{idade}')"""
            
            inst_cadastro.execute(cadastro)
            conn.commit()
            print("Dados gravados!")
        case 2:
            listar_dados = []
            inst_consulta.execute("SELECT * FROM petshop")
            data = inst_consulta.fetchall()
            
            for dt in data:
                listar_dados.append(dt)
            
            listar_dados = sorted(listar_dados)
            
            dados_df = pd.DataFrame.from_records(listar_dados, columns=['id', 'Tipo', 'Nome', 'Idade'], index='id')
            
            if dados_df.empty:
                print("Não há pets cadastrados!")
            else:
                # lista os dados 
                print(dados_df)
                
                gerar_planilha = input("Gerar Planilha? [S]im ou [N]ão: ").lower()
                if gerar_planilha == "s":
                    nome_arquivo = "planilha" + dia_hora
                    dados_df.to_excel(nome_arquivo+".xlsx", index=False)
                    print('Dados')
                else:
                    print("Não queria exportar mesmo...")