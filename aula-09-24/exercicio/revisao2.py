# RM 554456 - VINÍCIUS SAES DE SOUZA
import json

with open("dados.txt", "r") as file:
    dados = file.readlines()
    aux = []
    logins = []
    emails = []
    for i, string in enumerate(dados):
        aux = string.split(",")
        logins.append(aux[0].strip() + "\n")
        emails.append(aux[1].strip() + "\n")

logins_txt = open("logins.txt", "w+")
emails_txt = open("e-mails.txt", "w+")

logins_txt.writelines(logins)
emails_txt.writelines(emails)

logins_txt.seek(0)
emails_txt.seek(0)

print("\nlogin.txt")
print(logins_txt.read(), end="")
print("\ne-mails.txt")
print(emails_txt.read(), end="")

pessoas = {}
for i in range (0, len(logins), 1):
    pessoas[f"pessoa{i+1}"] = {'login' : logins[i].strip(), 'email' : emails[i].strip()}

with open("arquivo.json", "w+") as file:
    pessoas_json = json.dumps(pessoas, indent=4)
    file.writelines(pessoas_json)
    
    pessoas = json.loads(pessoas_json)
    print(pessoas)

logins_txt.close()
emails_txt.close()
  