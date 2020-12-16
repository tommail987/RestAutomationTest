import requests

custom_header = {'T1':'Header1', 'T2':'Header2'}
parameters = {'name':'TT', 'age':'56', 'email':'email@email34.com'}

response = requests.get('https://httpbin.org/get', headers=custom_header, params=parameters)
print(response.text)