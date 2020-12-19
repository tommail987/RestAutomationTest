import requests
from Utility.common import Common
import unittest

class Add_Multiple_Students_From_File(unittest.TestCase):

    def test_add_multiple_students_from_file(self):
        #variables
        url = 'http://thetestingworldapi.com/api/studentsDetails'
        request_file_path = 'DDT\\TestData\\newStudent.json'
        xslx_file_path = 'DDT\\TestData\\Students.xlsx'
        sheet = 'Arkusz1'

        #objects
        c = Common()


        json_file = c.request_file(request_file_path) # load json file into variable in json (dictionary) format
        row = c.fetch_row_count()
        key_list = c.fetch_key_names()

        for i in range(2, row+1): #for each row in range, without first row because there are headers
            updated_json_request = c.update_request_with_data(i, json_file, key_list)
            response = requests.post(url, updated_json_request)
            print(response.text)
            print(response.status_code)
            assert response.status_code == 201