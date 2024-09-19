import os
os.system("cls" if os.name == 'nt' else "clear")

import datetime

agora = datetime.datetime.now()
print(f"Formato chines: {agora}")
print(f"Formato brasileiro: {agora:%d/%m/%y - %a}")
print(f"Textual: {agora.ctime()}")

# definindo uma data
data = datetime.datetime(2024,5,29, 12, 15, 45, 8765)
print(data.hour)

dia = data.day
print (dia)
mes = data.month
print (mes)
ano = data.year
print (ano)

nova_data = data - datetime.timedelta(days = 1.5)
print(f"{data}\n{nova_data}")

hoje = datetime.date.today()
print(hoje)
hoje = datetime.date(2024, 5,5)
print(hoje)

hora = datetime.time(12,4,1)
print(hora)
print(hora.hour + 1)
print(hora.hour)
print(hora.minute + 1)
print(hora.second + 12)

