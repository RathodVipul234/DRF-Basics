import requests

URL ="http://127.0.0.1:8000/"

a = requests.get(url = URL)

data = a.json()

print(data)

