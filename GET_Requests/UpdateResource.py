import requests
import json
from jsonpath import jsonpath

url = 'https://reqres.in/api/users/2'

file = open('C:\\Users\\TT\\Desktop\\Test.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
print(requests_json)

response = requests.put(url, requests_json)
print(response.status_code)
assert response.status_code == 200

#Fetch header from response
print(response.headers)

#Parse response to json format
response_json = json.loads(response.text)

#Pick Id using jon path
responseName = jsonpath(response_json, 'name')
print(responseName[0])