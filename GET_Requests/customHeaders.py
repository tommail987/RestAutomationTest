import requests

custom_header = {'T1':'Header1', 'T2':'Header2'}
response = requests.get('https://httpbin.org/get', headers=custom_header)
print(response.text)