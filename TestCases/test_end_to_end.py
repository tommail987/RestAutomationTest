from jsonpath import jsonpath
import requests
import json

def test_add_new_data():
    url = 'http://thetestingworldapi.com/api/studentsDetails'
    file_path = 'C:\\Users\\TT\\Desktop\\newStudent.json'
    f = open(file_path, 'r')
    request_json = json.loads(f.read())
    response = requests.post(url, request_json)
    id = jsonpath(response.json(), 'id')
    print(id[0])

    urltechskills = 'http://thetestingworldapi.com/api/technicalskills'
    file_path_tech_skills = 'C:\\Users\\TT\\Desktop\\newStudent_techSkills.json'
    f = open(file_path_tech_skills, 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(urltechskills, request_json)
    print(response.text)

    urladdresses = 'http://thetestingworldapi.com/api/addresses'
    file_path_addresses = 'C:\\Users\\TT\\Desktop\\newStudent_address.json'
    f = open(file_path_addresses, 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(urladdresses, request_json)
    print(response.text)

    urlfinal = 'http://thetestingworldapi.com/api/FinalStudentDetails/{}'.format(id[0])
    response = requests.get(urlfinal)
    print(response.text)