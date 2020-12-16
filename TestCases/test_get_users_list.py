import requests
import json
import jsonpath
import pytest

url = 'https://reqres.in/api/users?page=2'

# def create_json_input_from_file(file_path):
#     file = open(file_path, 'r')
#     json_input = file.read()
#     requests_json = json.loads(json_input)
#     return requests_json

def test_get_users_list():
    response = requests.get(url)
    assert response.status_code == 200

    #Parse response to json format
    response_json = json.loads(response.text)

    #Pick Id using json path
    responseName = jsonpath.jsonpath(response_json, 'data[:3].first_name')
    print(responseName[:])