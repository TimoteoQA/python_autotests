import requests

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
json_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}
json_change = {
    "pokemon_id": "27986",
    "name": "VSCode",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
json_add_pokeball = {
    "pokemon_id": "27986"
}


'''response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = json_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = json_change)
print(response_change.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = json_add_pokeball)
print(response_add_pokeball.text)'''

