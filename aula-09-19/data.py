import os
os.system('cls' if os.name == 'nt' else 'clear')

import datetime

agora = datetime.datetime.now()

print(f"Formato chines: {agora}")
print(f"Fromato normal: {agora:%d/%m/%y - %a}")
print(f"Fromato textual: {agora.ctime()}")

date = datetime.datetime(2024, 5, 29,)
print(date)

dia = date.day
print(dia)

month = date.month
print(month)

year = date.year
print(year)

nova_data = date + datetime.timedelta(days = 7)
print(f"{date}\n{nova_data}")

hora_atual = (datetime.datetime.now()).hour

print(hora_atual)