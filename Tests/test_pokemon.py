import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = ''
TRAINER_NAME = ''

def test_status_code():
    response_trainers = requests.get(url = f'{URL}trainers', headers = HEADER)
    assert response_trainers.status_code == 200
def test_name_string():
    response_trainers = requests.get(url = f'{URL}trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_trainers.json()["data"][0]["trainer_name"] == TRAINER_NAME