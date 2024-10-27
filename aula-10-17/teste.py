from datetime import datetime 

data = datetime(2024, 8, 9)



data_f =data.strftime("%d/%m/%Y")

print(data_f)

# ano_mes_dia = str(datetime.now().date())
# ano_mes_dia = ano_mes_dia.replace("-", "")
# hora = str(datetime.now().hour) + (str)(datetime.now().minute) + (str)(datetime.now().second)
# data = ano_mes_dia + hora
# print(type(data))
