import json
import requests
import jsonpath

dict1 = '{"K1":"V1", "K2":"V2"}'

json_result = json.loads(dict1)
print(json_result)