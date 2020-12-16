import requests
from requests.auth import HTTPBasicAuth

def test_simple_auth():
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth('tommail987', '174d03fd7919c8471d6b86f834f864cedef1bea7'))
    print(response.text)