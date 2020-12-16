import requests
import json
import pytest
from jsonpath import jsonpath

#pytest.mark.skip('Skip for now')
def test_add_new_student():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    json_file_path = 'C:\\Users\\TT\\Desktop\\newJson.json'

    f = open(json_file_path, 'r')
    json_file = json.loads(f.read())
    json_request = requests.post(API_URL, json_file)
    response = json_request.json()
    print(response)
    assert json_request.status_code == 201
    global id
    id = jsonpath(response, 'id')
    id = id[0]
    print(id)


def test_get_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(id)
    print(API_URL)

    json_request = requests.get(API_URL)

    # Parse response to json format
    response = json_request.json()
    #response = json.loads(json_request.text)
    print(response)

    response_name = jsonpath(response, 'data.first_name')
    print(response_name[0])

def test_put_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(id)
    json_file_path = 'C:\\Users\\TT\\Desktop\\newJsonPut.json'

    f = open(json_file_path, 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_get_student_data_again():
    test_get_student_data()

def test_delete_student_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(id)

    json_request = requests.delete(API_URL)
    print(json_request.text)

def test_get_student_data_again1():
    test_get_student_data()