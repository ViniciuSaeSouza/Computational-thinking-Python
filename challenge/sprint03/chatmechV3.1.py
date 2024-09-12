import os
os.system("cls")
"""
Feedback: 
Permitiu cadastrar login e senha em branco. ✔️
Permitiu cadastro do veiculo em branco. ✔️
Ao digitar o horário do agendamento apareceu o erro: line 194, in acessar_usuário(). ✔️
A usabilidade e consistência dos dados devem ser melhoradas no geral. 
"""



#---------------------------------- Funções
class ExitProgram(Exception):
    pass

def voltar_menu_inicial(entrada:str):
  if entrada.lower() == 'sair':
    menu_inicial()
  
def voltar_menu_principal(entrada:str):
  if entrada.lower() == 'sair':
    menu_principal()
    
def voltar_menu_veiculo(entrada):
  if entrada.lower() == 'sair':
    os.system('cls')
    menu_veiculo()

def presione_qualquer_tecla_inicial():
  input("Digite qualquer tecla para voltar ao menu inicial: ")
  menu_inicial()
  
def presione_qualquer_tecla_principal():
  input("Digite qualquer tecla para voltar ao menu principal: ")
  menu_principal()
  
def menu_principal():
    os.system('cls')
    print(
          " -- CHATMECH --\n"
          "\n1 - Veiculos \n"
          "2 - Conversar com o Mechzinho \n"
          "3 - Serviços \n"
          "4 - Quem somos \n"
          "5 - Retornar a tela inicial\n"
          "6 - SAIR\n")
    while True:
        opcao = input("Escolha uma opção: ")
        match opcao:
          case '1':
            os.system("cls")
            menu_veiculo()
          case '2':
            print("\nBem vindo ao ChatMech, nosso mecânico virtual, qual o seu problema ?\n") # Aqui o programa irá retornar ao menu, pois só irá ter continuidade com a implementação do ChatBot
            input("\n Pressione qualquer tecla para voltar ao menu: ")
            menu_principal()  
          case '3':
            menu_servico()
            break
          case '4':
            os.system('cls')
            print("\nSomos uma solução rapida e prática para problemas mecânicos em geral, atendemos via internet por meio do Mechzinho, nosso ChatBot, onde ele fará uma série de perguntas sobre o problema de seu veiculo e por meio de sua inteligência ele será capaz de dar um diagnóstico da possivel solução e em quais mecânicas atendem o caso, além de dar um breve orçamento das peças necessárias para a manutenção, o preço é obtido por meio do mercado geral, podendo ter mudanças por região.")
            input("\n Pressione qualquer tecla para voltar ao menu: ")
            menu_principal()
            break
          case '5':
            menu_inicial()
            break
          case '6':
            print("Saindo....")
            exit()
          case _:
            print("\nOpção inválida! digite novamente.")


servicos = {
  'servico1': {'dia': 8, 'mes': 9, 'hora': '14:30'}
}


def mostra_servicos_agendados():
  if not servicos:
    print("Não há nenhum serviço cadastrado!")
  else:
    os.system('cls')
    print(" -- SERVIÇOS AGENDADOS -- \n")
    i = 1
    for servico, dados in servicos.items():
      dia = dados.get('dia')
      mes = dados.get('mes')
      
      if dia < 10:
        dia = "0" + str(dia)
      if mes < 10:
        mes = "0" + str(mes)
        
      print(f"\n- Serviço {i}: {dia}/{mes} ás {dados['hora']}hrs")
      i += 1
  input("\nPressione qualquer tecla para voltar: ")
  menu_servico()


def menu_servico():
    os.system('cls')
    print(" -- SERVIÇOS --")
    while True:
      opcao = input("""
1 - Agendar serviço
2 - Serviços agendados
3 - Menu principal

Escolha: """)
      match opcao:
        case "1":
          os.system('cls')
          agendar_servico()
        case "2":
          mostra_servicos_agendados()
          break
        case "3":
          menu_principal()
          break
        case _:
          print(" **ERRO! Digite uma opção válida**")
          
def agendar_servico():
    os.system('cls')
    while True:
        try:
            # Verifica o dia
            while True:
                try:
                    dia = int(input("Qual dia gostaria de agendar seu serviço?\nEscolha: "))
                    if not (1 <= dia <= 31):
                        raise ValueError("dia")
                    break  # Sai do loop quando o dia for válido
                except ValueError:
                    print("**ERRO! Dia deve estar entre 1 e 31.**")

            # Verifica o mês
            while True:
                try:
                    mes = int(input("\nQual o mês?\nEscolha: "))
                    if not (1 <= mes <= 12):
                        raise ValueError("mes")
                    break  # Sai do loop quando o mês for válido
                except ValueError:
                    print("**ERRO! Mês deve estar entre 1 e 12.**")

            # Verifica o horário
            while True:
                try:
                    hora = input("\nQual o horário do agendamento? (Formato hh:mm)\nEscolha: ")
                    hora_parts = hora.split(':')
                    if len(hora_parts) != 2 or not all(part.isdigit() for part in hora_parts):
                        raise ValueError("hora_formato")
                    
                    # Valida a hora e minuto
                    hora_int = int(hora_parts[0])
                    minuto_int = int(hora_parts[1])
                    if not (0 <= hora_int < 24 and 0 <= minuto_int < 60):
                        raise ValueError("hora_valor")
                    break  # Sai do loop quando o horário for válido
                except ValueError as e:
                    if str(e) == "hora_formato":
                        print("**ERRO! O horário deve estar no formato hh:mm.**")
                    elif str(e) == "hora_valor":
                        print("**ERRO! Horário inválido. Hora deve estar entre 00:00 e 23:59.**")
            break  # Sai do loop geral se todos os dados forem válidos
        
        except Exception as e:
            os.system("cls")
            print(f"Erro inesperado: {e}")
    
    servicos[f"servico{len(servicos)+1}"] = {'dia':dia,'mes':mes,'hora':hora}
    
    # Aqui segue o fluxo normal após o agendamento correto
    print(f"Serviço agendado para {dia}/{mes} às {hora}.")
        
def acessar_usuario():
    try:
        while True:
            print("\n1 - Registrar usuário\n"
                "2 - Fazer login\n"
                "3 - Encerrar programa\n")
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1: # Irá chamar a tela de registro de usuário
                    os.system("cls")
                    registrar_usuario()
                elif opcao == 2: # Irá chamar a tela de login
                    os.system("cls")
                    if verificar_login():
                        print("Acesso concedido")

                    else:
                        os.system("cls")
                        print("Acesso negado, você não possui uma conta registrada...\n"
                            "Por favor, Registre-se aqui: \n")
                        return registrar_usuario()
                elif opcao == 3: # Sairá do programa
                    print("Saindo...")
                    exit()
                else:
                    print("Opção inválida. Tente novamente.\n")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")
                os.system("cls")
    except ExitProgram:
        print("Programa encerrado.")

def verifica_input_vazio(pergunta:str, tipo:str) -> str:
    while(True):
        entrada = ""
        entrada = input(f"Digite 'sair' para voltar ao menu --\n{pergunta}")
        if tipo == 'i':
          voltar_menu_inicial(entrada)
        elif tipo == 'p':
          voltar_menu_principal(entrada)
        elif tipo == 'v':
          voltar_menu_veiculo(entrada)
        if entrada == "":
          print("ERRO! campo não pode estar vazio!")
        else:
          os.system('cls')
          break
    return entrada

usuarios = {  # Um dicionário que armazena os dados de login e senha
  'usuario1': 
    {
      'login':'saes', 
      'senha':'saes'
    }
}
def verifica_se_existe(dado:str,chave:str,dicionario:dict) -> bool:
  for k, v in dicionario.items():
    if dado == v[chave]:
      return True
    else:
      return False
    # break  # Sai do loop se a placa não existir

def registrar_usuario():
    print("Bem vindo, Cadastre-se em nosso sistema: \n")
    login = ""
    login = verifica_input_vazio("Digite o login: ", 'i')
    while verifica_se_existe(login, 'login', usuarios):
      print("ERRO! Usuário já cadastrado.\n")
      login = verifica_input_vazio("Digite o login: ", 'i')
    
    
    def verifica_senha_valida() -> str:
      while True:
        senha = verifica_input_vazio("Digite a senha: ", 'i')
        if len(senha) < 5:
          print("**ERRO! Senha deve possuir no mínimo 5 caracteres**\n")
        else:
          return senha
    
    senha = verifica_senha_valida()
      
    
    usuarios[len(usuarios)+1] = {'login': login, 'senha': senha}
    print("\nUsuário registrado com sucesso!\n")
    return verificar_login()

def verificar_login():
    print("Para realizar seu login, preencha as informações abaixo:\n")
    login = verifica_input_vazio("Digite seu login: ", 'i')
    senha = verifica_input_vazio("Digite sua senha: ", 'i')
    
    for usuario, dados in usuarios.items():# Aqui o usuário terá que digitar o mesmo login e senha que foi digitado na tela de registro, pois é a informação que está armazenada na lista, caso digite outra informação, resultará em dados incorretos, e ficará dando loop até digitar as informações dadas no registro
        if dados['login'] == login and dados['senha'] == senha:
            print("Login bem-sucedido!")
            os.system("cls")                
            menu_principal()
    os.system('cls')
    print("\nLogin ou senha incorretos.\n")
    return True


veiculos = {'veiculo1': {'placa': 'DPX1018', 'modelo': 'fuxca', 'dono': 'dodock'},
            'veiculo2': {'placa': 'XXT2020', 'modelo': 'polo', 'dono': 'saes'}} # Um dicionário que armazena os dados do veiculo
# veiculos = {}      
def verifica_placa_valida() -> str:
    while True:
        placa = verifica_input_vazio("Digite a placa do veículo: ", 'v').upper()
        if len(placa) != 7:
            print("ERRO! Placa deve ter 7 dígitos")
        else:
            return placa

def mostrar_veiculos():
  if veiculos:
    i = 1
    print("\nVeículos cadastrados:\n")
    for veiculo, dados in veiculos.items():
      print(f"Veiculo {i}- ")
      print(f"Placa: {dados['placa']}\nModelo: {dados['modelo']}\nDono: {dados['dono']}\n")
      i += 1
  else:
    print("\nNenhum veículo cadastrado.\n")
    input("Pressione qualquer tecla para voltar ao menu de veículos: ")
    os.system('cls')
    menu_veiculo()
        
def cadastrar_veiculo():
    placa = verifica_placa_valida()
    while verifica_se_existe(placa, 'placa', veiculos):
      print("ESTE DADO JÁ EXISTE!")
      placa = verifica_placa_valida()

    modelo = verifica_input_vazio("Digite o modelo do seu veículo: ", 'p')
    dono = verifica_input_vazio("Digite o nome do dono do veículo: ", 'p')

    veiculo = {'placa': placa, 'modelo': modelo, 'dono': dono}

    veiculos[f'veiculo{len(veiculos)+1}'] = veiculo
    print("\nVeículo cadastrado com sucesso!\n")

  

def excluir_veiculo():
  os.system('cls')
  selecao_valida = False
  while True:
    mostrar_veiculos()
    while True:
      selecao = verifica_input_vazio("Digite o número do veículo a ser excluído: ", 'v')
      if not selecao.isdigit():
        mostrar_veiculos()
        print("Número do veículo inexistente!")
        continue
      else:
        chave = 'veiculo' + selecao
        confirmacao = input(f"Tem certeza que deseja excluir {chave}? (s/n): ").lower()
        break
    match confirmacao:
      case 's':
        atualiza_chaves_dicionario(veiculos)
        # Excluir o veículo
        del veiculos[chave]
        print("Veículo excluído com sucesso!")
        input("Pressione qualquer tecla para voltar ao menu de veículo: ")
        os.system('cls')
        menu_veiculo()
      case 'n':
        os.system('cls')
        menu_veiculo()
        break
      
def atualiza_chaves_dicionario(dicionario:dict) -> None:
  veiculos_copy = {}
  for i, (veiculo, dados) in enumerate(dicionario.items()):
    veiculos_copy[f"veiculo{i+1}"] = dados
  
  veiculos.clear()
  veiculos.update(veiculos_copy)

def editar_veiculo():
  os.system('cls')
  selecao_valida = False
  while True:
    while selecao_valida == False:
      mostrar_veiculos()
      try:
        selecao = verifica_input_vazio("Digite o número do veículo a ser alterado: ", 'v')
        if int(selecao) > len(veiculos) or int(selecao) < 1:
          print("Não existe veículo com este número!")
        else:
          os.system('cls')
          selecao_valida = True
          break
      except:
        print("Erro! digite um número válido")
    chave = 'veiculo' + selecao
    veiculo_selecionado = veiculos.get(chave)
    placa = veiculo_selecionado['placa']
    modelo = veiculo_selecionado['modelo']
    dono = veiculo_selecionado['dono']
    dado_alterar = ""
      
    print(f"""Dados veículo -
Placa: {placa}
Modelo: {modelo}
Dono: {dono}
""")
    dado_alterar = verifica_input_vazio("Qual dado deseja alterar (placa, modelo, dono): ", 'v').lower()
    voltar_menu_principal(dado_alterar)
    match dado_alterar:
      case "placa":
        print(f"Placa atual: {placa}")
        nova_placa = verifica_placa_valida()
        veiculo_selecionado['placa'] = nova_placa
        veiculos[chave] = veiculo_selecionado
        placa = nova_placa
      case "modelo":
        print(f"Modelo atual: {modelo}")
        novo_modelo = verifica_input_vazio("Novo modelo: ", 'v').lower()
        veiculo_selecionado['modelo'] = novo_modelo
        veiculos[chave] = veiculo_selecionado
        modelo = novo_modelo
      case "dono":
        print(f"Dono atual: {dono}")
        novo_dono = verifica_input_vazio("Novo dono: ", 'v').lower()
        veiculo_selecionado['dono'] = novo_dono
        dono = novo_dono
      case _:
        print("Opção inválida!")
    while True:
      alterar_mais = input("Deseja alterar mais algum item?\nEscolha (S/N): ").lower()
      match alterar_mais:
        case "s":
          break
        case "n":
          os.system('cls')
          menu_veiculo()
          break
        case _:
          print("Opção inválida!")


def menu_veiculo(): #CRUD
  while True:
    print(""" -- MENU VEÍCULOS --
   
1 - Cadastrar veículo
2 - Mostrar veículos cadastrados
3 - Editar veículo
4 - Excluir veículo
5 - Voltar ao menu principal
""")
    opcao = input("Escolha uma opção: ")
    match opcao:        
      case "1":
        os.system("cls")
        cadastrar_veiculo()
      case "2":
        os.system('cls')
        mostrar_veiculos()
        input("Pressione qualquer tecla para voltar ao menu de veículos: ")
        os.system('cls')
        menu_veiculo()
        break
      case "3":
        editar_veiculo()
        os.system('cls')
        break
      case "4":
        os.system('cls')
        excluir_veiculo()
        break
      case "5":
        menu_principal()
        break
      case _:
        print("Opção inválida. Tente novamente.")
#---------------------------------- Programa principal


def menu_inicial():
  os.system("cls")
  print("Bem vindo ao ChatMech, acesse sua conta: \n")
  print("0 - SAIR\n1 - Acessar ou Cadastrar usuário\n2 - Acessar o Mechzinho sem cadastro\n")

  while True:
    opcao = input("\nEscolha uma opção: ")
    if opcao != "":  
      match opcao:
        case "0":
          os.system('cls')
          print("Saindo...")
          exit()
          break
        case "1":
          acessar_usuario()
          break
        case "2":
          os.system('cls')
          print("Bem vindo ao ChatMech, nosso mecânico virtual, qual o seu problema?")
          presione_qualquer_tecla_inicial()
          break
        case _:
          print("ERRO! Digite uma opção válida.")
    else:
      print("ERRO! Digite uma opção válida")
      
menu_inicial()
# menu_principal()
   