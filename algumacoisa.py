import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon/42')
print(response.status_code)
print(response.json())