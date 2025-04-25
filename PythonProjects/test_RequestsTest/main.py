import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN =  "*"
HEADER = {"Content-type" : "application/json", "trainer_token" : TOKEN}

body_create = {

    "name": "Бульбазавр",

    "photo_id": 1 }

body_name_change = {
    "pokemon_id": "301314",
    "name": "New Name",
    "photo_id": 2
}

body_pokemon_add_pokeball= {
    "pokemon_id": "301314"
}

response_create = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_create)
print(response_create.text)

response_name_change = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = body_name_change)
print(response_name_change.text)

response_pokemon_add_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_pokemon_add_pokeball)
print(response_pokemon_add_pokeball.text)