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
    def test_only_odds(self):
        '''
        OnlyOdds([1,2,3,4,5]) should return [1,3,5]
        '''
        funName = 'OnlyOdds'
        testval1 = [1,2,3,4,5]
        expected = [1,3,5]
        result = TestWeek8.STUDENT[funName](testval1)
        self.assertEqual(result, expected) 

    @weight(1)
    def test_sum_100(self):
        ''' 
        Sum100([1,2,3,4,5]) should return 15
        '''
        funName = 'Sum100'
        testval1 = [1,2,3,4,5]
        expected = 15
        msg = "Sum100([1,2,3,4,5]) should return 15"
        result = TestWeek8.STUDENT[funName](testval1)
        self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_sum_100_2(self):
        ''' 
        Sum100([20,20,50]) should return 90
        '''
        funName = 'Sum100'
        testval1 = [20,20,50]
        expected = 90 
        msg = funName + "(" + str(testval1) + ") should return" + str(expected)
        result = TestWeek8.STUDENT[funName](testval1)
        self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_sum_100_3(self):
        ''' 
        Sum100([1000]) should return 1000
        '''
        funName = 'Sum100'
        testval1 = [1000]
        expected = 1000 
        msg = funName + "(" + str(testval1) + ") should return" + str(expected)
        result = TestWeek8.STUDENT[funName](testval1)
        self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_class_average(self):
       '''
       ClassAverage([10,20,30]) should be 20.0
       '''
       funName = 'ClassAverage'
       testval1 = [10,20,30]
       expected = 20.0
       result = TestWeek8.STUDENT[funName](testval1)
       self.assertEqual(result, expected) 

    @weight(1)
    def test_adjust_grades(self):
       '''
       AdjustGrades([10,20,30],20) --> [30, 40, 50]
       '''
       funName = 'AdjustGrades'
       testval1 = [10,20,30]
       testval2 = 20
       expected = [30,40,50]
       result = TestWeek8.STUDENT[funName](testval1,testval2)
       self.assertEqual(result, expected) 


    @weight(1)
    def test_curve_grades(self):
       '''
       CurveGrades([85,62,70,30]) -> [100, 77, 85, 45]
       '''
       funName = 'CurveGrades'
       testval1 = [85,62,70,30] 
       expected = [100, 77, 85, 45]
       result = TestWeek8.STUDENT[funName](testval1)
       self.assertEqual(result, expected) 


    @weight(1)
    def test_curve_grades2(self):
       '''
       CurveGrades([85,60,76,130,80]) -> [55, 30, 46, 100, 50]
       '''
       funName = 'CurveGrades'
       testval1 = [85,60,76,130,80]
       expected = [55, 30, 46, 100, 50]
       result = TestWeek8.STUDENT[funName](testval1)
       self.assertEqual(result, expected) 
     