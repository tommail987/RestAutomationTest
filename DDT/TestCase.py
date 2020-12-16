import requests
import json
import common

def test_add_multiple_students():
    #API
    url = 'http://thetestingworldapi.com/api/studentsDetails'
    file_path = 'C:\\Users\\TT\\Desktop\\Test\\newStudent.json'
    f = open(file_path, 'r')
    json_file = json.loads(f.read())  # load json file into variable in json (dictionary) format

    obj = common.Common('C:\\Users\\TT\\Desktop\\Test\\Students.xlsx', 'Arkusz1')
    row = obj.fetch_row_count()
    key_list = obj.fetch_key_names()


    for i in range(2, row+1): #for each row in range, without first row because there are headers
        updated_json_request = obj.update_request_with_data(i, json_file, key_list)
        response = requests.post(url, updated_json_request)
        print(response.text)
        print(response.status_code)
        assert response.status_code == 201