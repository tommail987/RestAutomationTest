import requests
import json
import jsonpath
import pytest

url = 'https://reqres.in/api/users'
a=11
json_file_path = 'C:\\Users\\TT\\Desktop\\Test.json'

def create_json_input_from_file(file_path):
    file = open(file_path, 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    return requests_json

def test_create_user():
    json_input = create_json_input_from_file(json_file_path)

    response = requests.post(url, json_input)
    assert response.status_code == 201

    #Parse response to json format
    response_json = json.loads(response.text)

    #Pick Id using jon path
    responseName = jsonpath.jsonpath(response_json, 'id')
    print(responseName[0])

@pytest.mark.skipif(condition=a>10, reason='This TC is not ready for test')
def test_create_other_user():
    file = open('C:\\Users\\TT\\Desktop\\Test.json', 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)

    response = requests.post(url, requests_json)
    print(response.status_code)
    assert response.status_code == 201

    #Fetch header from response
    print(response.headers)

    #Parse response to json format
    response_json = json.loads(response.text)

    #Pick Id using jon path
    responseName = jsonpath.jsonpath(response_json, 'id')
    print(responseName[0])