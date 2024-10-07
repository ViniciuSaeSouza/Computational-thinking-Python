import requests

url_personagens = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url_personagens)

personagens_json:dict = resposta.json()

nome = input("Nome: ")
for personagens in personagens_json["results"]:
	if personagens["name"] == nome:
		print(f"""Nome: {personagens["name"]}
Status: {personagens["status"]}
Espécie: {personagens["species"]}
Gênero: {personagens["gender"]}
Origem: {personagens["origin"]["name"]}""")
