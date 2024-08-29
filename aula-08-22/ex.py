alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]

lista_nome = []

def verifica_lista(a):
  if a == []:
    return False
  else:
    return True
  
def excluir_nome():
  if verifica_lista() == True:
    print(f"Nome excluído")
  else:
    print("Po, preenche um nome primeiro né")
    
