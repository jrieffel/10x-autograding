import unittest
#from unittest import mock
import re
import sys
from io import StringIO
from gradescope_utils.autograder_utils.decorators import weight, tags
from unittest import mock
import subprocess
import math


class TestWeek8(unittest.TestCase):

    MARKER = "### DO NOT DELETE THIS LINE: beg testing"
    STUDENT = {} # namespace of student code

    @classmethod
    def setUpClass(cls):
         try:
             student_code = open('practiceQuiz2.py','rt').read()
             student_code = student_code.split(cls.MARKER)[0]
             exec(student_code, cls.STUDENT)
         except:
             exec("", cls.STUDENT)






    @weight(1)
    def test_sum_100(self):
        ''' 
        Sum100([1,2,3,4,5]) should return 15
        '''
        funName = 'Sum100'
        testval1 = [1,2,3,4,5]
        expected = 15
        msg = "Sum100([1,2,3,4,5]) should return 15"
        result = TestWeek8.STUDENT[funName](testval1,testval2)
        self.assertEqual(result, expected, msg=msg)


     