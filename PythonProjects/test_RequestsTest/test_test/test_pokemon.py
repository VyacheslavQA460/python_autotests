import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN =  "7c3041c6d4c7d9f3cd9e815c0b8ce4d4"
HEADER = {"Content-type" : "application/json", "trainer_token" : TOKEN}
TRAINER_ID = "29209"

def test_code():
    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_trainer():

    response_trainer = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert response_trainer.json()["data"][0] ["id"] == TRAINER_ID
   