# instalacao do pip https://medium.com/@nara.guimaraes/instalando-o-pip-nolinux-windows-e-macos-um-guia-passo-a-passo-cc7b6d752b31#:~:text=Instalação%20do%20Pip%20no%20macOS,Python%203%20e%20o%20Pip.
 
# Importação dos módulos
import os
import oracledb
 
# import cx_Oracle ============> COMENTEM ESTA LINHA
import pandas as pd
 
# Try para tentativa de Conexão com o Banco de Dados
try:
    # Conecta o servidor
    # dsnStr = cx_Oracle.makedsn("oracle.fiap.com.br", "1521", "ORCL") ============> COMENTEM ESTA LINHA
    # Efetua a conexao com o Usuário
    # ==================> ADD A LINHA DE BAIXO
    conn = oracledb.connect(user="pf1530", password="fiap2024", dsn='oracle.fiap.com.br:1521/ORCL')
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a Aplicação
    conexao = True
 
margem = ' ' * 4  # Define uma margem para a exibição da aplicação
 
# Enquanto o flag conexao estiver apontado com True
while conexao:
    # Limpa a tela via SO
    os.system('clear')
 
    # Apresenta o menu
    print("------- CRUD - PETSHOP -------")
    print("""
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Alterar Pet
    4 - Excluir Pet
    5 - EXCLUIR TODOS OS PETS
    6 - SAIR
    """)
 
    # Captura a escolha do usuário
    escolha = input(margem + "Escolha -> ")
 
    # Verifica se o número digitado é um valor numérico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        escolha = 6
        print("Digite um número.Reinicie a Aplicação!")
 
    os.system('clear')  # Limpa a tela via SO
 
    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
        # CADASTRAR UM PET
        case 1:
            try:
                print("----- CADASTRAR PET -----")
                # Recebe os valores para cadastro
                tipo = input(margem + "Digite o tipo....: ")
                nome = input(margem + "Digite o nome....: ")
                idade = int(input(margem + "Digite a idade...: "))
 
                # Monta a instrução SQL de cadastro em uma string
                cadastro = f"""
                INSERT INTO petshop (tipo_pet, nome_pet, idade)
                VALUES ('{tipo}', '{nome}', {idade})
                """
 
                # Executa e grava o Registro na Tabela
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                # Erro de número não digitar um numero na idade
                print("Digite um número na idade!")
            except:
                # Caso ocorra algum erro de conexão ou no BD
                print("Erro na transação do BD")
            else:
                # Caso haja sucesso na gravação
                print("##### Dados GRAVADOS #####")
 
        # LISTAR TODOS OS PETS
        case 2:
            print("----- LISTAR PETs -----")
            lista_dados = []  # Lista para captura de dados do Banco
 
            # Monta a instrução SQL de seleção de todos os registros da tabela
            inst_consulta.execute('SELECT * FROM petshop')
            # Captura todos os registros da tabela e armazena no objeto data
            data = inst_consulta.fetchall()
 
            # Insere os valores da tabela na Lista
            for dt in data:
                lista_dados.append(dt)
 
            # ordena a lista
            lista_dados = sorted(lista_dados)
 
            # Gera um DataFrame com os dados da lista utilizando o Pandas
            dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')
 
            # Verifica se não há registro através do dataframe
            if dados_df.empty:
                print(f"Não há um Pets cadastrados!")
            else:
                print(dados_df)  # Exibe os dados selecionados da tabela
 
            print("##### LISTADOS! #####")
 
        # ALTERAR OS DADOS DE UM REGISTRO
        case 3:
            try:
                # ALTERANDO UM REGISTRO
                print("----- ALTERAR DADOS DO PET -----")
 
                lista_dados = []  # Lista para captura de dados da tabela
 
                # Permite o usuário escolher um Pet pelo id
                pet_id = int(input(margem + "Escolha um Id: "))
 
                # Constroi a instrução de consulta para verificar a existencia ou não do id
                consulta = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                # Preenche a lista com o registro encontrado (ou não)
                for dt in data:
                    lista_dados.append(dt)
 
                # analisa se foi encontrado algo
                if len(lista_dados) == 0:  # se não há o id
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                    input("Pressione ENTER")
                else:
                    # Captura os novos dados
                    novo_tipo = input(margem + "Digite um novo tipo: ")
                    novo_nome = input(margem + "Digite um novo nome: ")
                    nova_idade = input(margem + "Digite uma nova idade: ")
 
                    # Constroi a instrução de edição do registro com os novos dados
                    alteracao = f"""
                    UPDATE petshop
                    SET tipo_pet='{novo_tipo}', nome_pet='{novo_nome}', idade='{nova_idade}'
                    WHERE id={pet_id}
                    """
                    inst_alteracao.execute(alteracao)
                    conn.commit()
            except ValueError:
                print("Digite um número na idade!")
            except:
                print(margem + "Erro na transação do BD")
            else:
                print("##### Dados ATUALIZADOS! #####")
 
        # EXCLUIR UM REGISTRO
        case 4:
            print("----- EXCLUIR PET -----")
            lista_dados = []  # Lista para captura de dados da tabela
            # Permite o usuário escolher um Pet pelo ID
            pet_id = input(margem + "Escolha um Id: ")
            if pet_id.isdigit():
                pet_id = int(pet_id)
                consulta = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                # Insere os valores da tabela na lista
                for dt in data:
                    lista_dados.append(dt)
 
                # Verifica se o registro está cadastrado
                if len(lista_dados) == 0:
                    print(f"Não há um pet cadastrado com o ID = {pet_id}")
                else:
                    # Cria a instrução SQL de exclusão pelo ID
                    exclusao = f"DELETE FROM petshop WHERE id={pet_id}"
                    # Executa a instrução e atualiza a tabela
                    inst_exclusao.execute(exclusao)
                    conn.commit()
                    # Exibe mensagem caso haja sucesso
                    print("##### Pet APAGADO! #####")
            else:
                print("O Id não é numérico!")
 
        # EXCLUIR TODOS OS REGISTROS
        case 5:
            print("!!!!! EXCLUI TODOS OS DADOS TABELA !!!!!")
            confirma = input(
                margem + "CONFIRMA A EXCLUSÃO DE TODOS OS PETS? [S]im ou [N]ÃO?")
            if confirma.upper() == "S":
                # Apaga todos os registros
                exclusao = "DELETE FROM petshop"
                inst_exclusao.execute(exclusao)
                conn.commit()
 
                # Depois de excluir todos os registros ele zera o ID
                data_reset_ids = """ ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                inst_exclusao.execute(data_reset_ids)
                conn.commit()
 
                print("##### Todos os registros foram excluídos! #####")
            else:
                print(margem + "Operação cancelada pelo usuário!")
 
        # SAI DA APLICAÇÃO
        case 6:
            # Modificando o flag da conexão
            conexao = False
 
        # CASO O NUMERO DIGITADO NÃO SEJA UM DO MENU
        case _:
            input(margem + "Digite um número entre 1 e 6.")
 
    # Pausa o fluxo da aplicação para a leitura das informações
    input(margem + "Pressione ENTER")
else:
    print("Obrigado por utilizar a nossa aplicação! :)")