import requests
import json
import jsonpath

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

# print(response)
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))
# print(response.elapsed)
# print(response.cookies)
# print(response.content)

# print(response.status_code)
# assert response.status_code == 200

# Parse response to json

json1 = json.loads(response.text)

#fetch value using jsonpath
pages = jsonpath.jsonpath(json1, 'data[:3].first_name')
print(pages)
assert pages[2] == 'Tobias'