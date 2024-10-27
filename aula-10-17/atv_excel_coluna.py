import os
import oracledb
import pandas as pd
import datetime


def cria_dataframe_todas_colunas() -> pd.DataFrame:
    lista_dados = []
    inst_consulta.execute("SELECT * FROM tbl_petshop")
    data = inst_consulta.fetchall()

    for dt in data:
        lista_dados.append(dt)

    lista_dados = sorted(lista_dados)

    dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade', 'Data Nascimento'])

    return dados_df

try:
    conn = oracledb.connect(user="RM558843", password="030306", dsn='oracle.fiap.com.br:1521/ORCL')

    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as e:
    conexao = False
else:
    conexao = True

while conexao:
    os.system("cls")
    print("""
    0 - Sair
    1 - Cadastrar
    2 - Listar / exportar
    3 - Selecionar as colunas
    selecionar as linhas
    exportar pro excel
    """)
    
    escolha = int(input("Escolha: "))
    match escolha:
        case 0:
            conexao = False
        case 1:
            tipo = input("\nTipo.......: ")
            nome = input("Nome.......: ")
            idade = int(input("Idade......: "))
            
            cadastro = f"""
            INSERT INTO tbl_petshop (tipo_pet, nome_pet, idade) 
            VALUES ('{tipo}', '{nome}', {idade})
            """
            inst_cadastro.execute(cadastro)
            conn.commit()
            print("\nDados gravados!")
            # input("\nPressione ENTER para continuar...")
        case 2:
            lista_dados = []
            inst_consulta.execute("SELECT * FROM tbl_petshop")
            data = inst_consulta.fetchall()

            for dt in data:
                lista_dados.append(dt)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade', 'Data Nascimento'])

            if dados_df.empty:
                print("\nNão há pets cadastrados!")
            else:
                # lista os dados
                print("\n=== Lista de Pets Cadastrados ===\n")
                print(dados_df)

                # Gera a planilha
                gerar_planilha = input("\nGerar Planilha? [s]im ou [n]ão? ")
                if gerar_planilha.lower() == 's':
                    data = datetime.datetime.now()
                    # nome_arquivo = input("\nNome do arquivo: ") or "planilha"
                    nome_arquivo = ("planilha" + f"{data.year}{data.month}{data.day}{data.hour}{data.minute}{data.second}")
                    dados_df.to_excel(nome_arquivo + ".xlsx", index=False)
                    print("\nPlanilha gerada com sucesso!")
            
            # SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'TBL_PETSHOP'

        case 3:

            colunas_exibir = []

            while True:
                os.system("cls")
                print("=== Escolha as Colunas a Exibir ===")
                print("""
                1 - Id
                2 - Tipo de Pet
                3 - Nome
                4 - Idade
                5 - Data de Nascimento
                6 - Todas
                7 - Finalizar
                """)
                
                escolha_coluna = input("Escolha: ")

                if escolha_coluna == '7':
                    break
                
                if escolha_coluna == '6': 
                    colunas_exibir = ['Id', 'Tipo', 'Nome', 'Idade', 'Data Nascimento']
                    print("Todas as colunas adicionadas.")
                    break
                
                match escolha_coluna:
                    case '1':
                        colunas_exibir.append('Id')
                        print("Coluna 'Id' adicionada.")
                    case '2':
                        colunas_exibir.append('Tipo')
                        print("Coluna 'Tipo' adicionada.")
                    case '3':
                        colunas_exibir.append('Nome')
                        print("Coluna 'Nome' adicionada.")
                    case '4':
                        colunas_exibir.append('Idade')
                        print("Coluna 'Idade' adicionada.")
                    case '5':
                        colunas_exibir.append('Data Nascimento')
                        print("Coluna 'Data de Nascimento' adicionada.")
                    case _:
                        print(f"Opção '{escolha_coluna}' inválida.")
                input("\nPressione enter para adicionar mais colunas... ")

            if colunas_exibir: # se existem colunas na lista
                dados_df = cria_dataframe_todas_colunas()
                dados_filtrados = dados_df[colunas_exibir]
                print("\n=== Registros Filtrados ===\n")
                print(dados_filtrados)
            input("\nPressione enter para continuar... ")
