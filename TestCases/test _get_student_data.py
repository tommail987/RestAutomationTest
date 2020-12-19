import requests
from Utility.common import Common
import unittest

class Get_Student_Data(unittest.TestCase):

    def test_get_student_data(self):
        # variables
        url = 'http://thetestingworldapi.com/api/studentsDetails'
        request_file_path = 'DDT\\TestData\\newStudent.json'

