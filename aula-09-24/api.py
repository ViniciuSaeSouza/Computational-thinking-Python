from tkinter import *
import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
def pegar_cotacoes():
  requisicao = requests.get(url)
  requisicao_dic = requisicao.json()
  cotacao_dolar = requisicao_dic['USDBRL']['bid']
  cotacao_euro = requisicao_dic['EURBRL']['bid']
  cotacao_btc = requisicao_dic['BTCBRL']['bid']
  texto_resposta['text'] = f"""
  Dólar: {cotacao_dolar}
  Euro: {cotacao_euro}
  BCT: {cotacao_btc}
  """
  # print(resposta)

#Desenhando a janela
janela = Tk()
janela.title("Cotações")
texto = Label(janela, text = "Clique aqui")
texto.grid(column=0, row=0, padx=10, pady= 10)
botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()