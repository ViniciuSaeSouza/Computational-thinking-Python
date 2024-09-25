import json
from xml.etree.ElementTree import indent

with open("dados.txt", "w") as file:
    file.writelines("""12345t, edson@fiap.com.br
01020d, maria@hotmail.com
1abcde, estela@ig.com.br
123abd, vania@terra.com.br""")

with open("dados.txt", "r") as file:
    dados = file.readlines()
    logins = []
    emails = []
    aux = []
    for i in range(0, len(dados), 1):
        aux = dados[i].split(",")
        logins.append(aux[0].strip() + "\n")
        emails.append(aux[1].strip() + "\n")


login_txt = open("login.txt", "w+")
email_txt = open("e-mail.txt", "w+")

login_txt.writelines(logins)
email_txt.writelines(emails)

login_txt.seek(0)
email_txt.seek(0)

print("login.txt")
print(login_txt.read(), end='\n')

print("e-mail.txt")
print(email_txt.read(), end='\n')

login_txt.seek(0)
email_txt.seek(0)
logins = login_txt.readlines()
emails = email_txt.readlines()
pessoas = {}
for i in range(0, len(logins)):
    pessoas[f"pessoa {i+1}"] = {'login' : logins[i].strip(), 'email' : emails[i].strip()}

print(pessoas)


with open("arquivo.json", "w+") as file:
    pessoas_json = json.dumps(pessoas, indent=4)
    file.writelines(pessoas_json)


login_txt.close()
email_txt.close()
