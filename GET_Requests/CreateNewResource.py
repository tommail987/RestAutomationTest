import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'

file = open('C:\\Users\\TT\\Desktop\\Test.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)

print(requests_json)

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