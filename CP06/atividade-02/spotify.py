from dotenv import load_dotenv
import os
import requests
import json
import base64

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

def get_token() -> str:
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
		"Authorization" : "Basic " + (auth_base64),
		"Content-Type" : "application/x-www-form-urlencoded"
	}
    
    data = {
		"grant_type" : "client_credentials"
	}
    
    result = requests.post(url, headers = headers, data = data)
    result_json = json.loads(result.content)
    token = result_json["access_token"]
    
    return token

token = get_token()

print(token)

