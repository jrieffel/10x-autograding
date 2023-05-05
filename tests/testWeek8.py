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
             student_code = open('quiz3.py','rt').read()
             student_code = student_code.split(cls.MARKER)[0]
             exec(student_code, cls.STUDENT)
         except:
             exec("", cls.STUDENT)






    @weight(1)
    def test_smaller1(self):
            ''' for the list [1,2,3,4,5,6,7,8,9,10], and val 3, should return 2'''
            testval1 = [1,2,3,4,5,6,7,8,9,10]
            testval2 = 3
            expected = 2
            msg = " SmallerThanCount: for the list [1,2,3,4,5,6,7,8,9,10], and val 3, should return 2"
            result = TestWeek8.STUDENT['SmallerThanCount'](testval1,testval2)
            self.assertEqual(result, expected, msg=msg)


    @weight(1)
    def test_smaller2(self):
            ''' for the list [1,2,3,4,5,6,7,8,9,10], and val -3, should return 0'''
            testval1 = [1,2,3,4,5,6,7,8,9,10]
            testval2 = -3
            expected = 0
            msg = "SmallerThanCount:  for the list [1,2,3,4,5,6,7,8,9,10], and val -3, should return 0"
            result = TestWeek8.STUDENT['SmallerThanCount'](testval1,testval2)
            self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_smaller3(self):
            ''' for the list [1,2,3,4,5,6,7,8,9,10], and val 8, should return 7'''
            testval1 = [1,2,3,4,5,6,7,8,9,10]
            testval2 = 8
            expected = 7
            msg = "SmallerThanCount:  for the list [1,2,3,4,5,6,7,8,9,10], and val 8, should return 7"
            result = TestWeek8.STUDENT['SmallerThanCount'](testval1,testval2)
            self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_Lottery(self):
            ''' Lottery(7) should return a list of 7 items between 0 and 9 '''
            testval = 7
            expected = 7
            msg = " Lottery() should return a list of 7 items between 0 and 9"
            result = TestWeek8.STUDENT['Lottery'](testval)
            result = len(result)
            self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_Lottery2(self):
            ''' Lottery(1) should return a list of 1 items between 0 and 9 '''
            testval = 1
            expected = 1
            msg = " Lottery(1) should return 1 a list of items between 0 and 9"
            result = TestWeek8.STUDENT['Lottery'](testval)
            result = len(result)
            self.assertEqual(result, expected, msg=msg)

    @weight(1)
    def test_Swap(self):
        '''Swap([1,2,3,4,5],0,4) should return [5,2,3,4,1]'''
        testval = [1,2,3,4,5] 
        i = 0
        j = 4
        msg = "Swap([1,2,3,4,5],0,4) should return [5,2,3,4,1]"
        expected = [5,2,3,4,1]
        result = TestWeek8.STUDENT['Swap'](testval,i,j)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_Swap2(self):
        '''Swap([1,2,3,4,5],1,3) should return [1,4,3,2,5]'''
        testval = [1,2,3,4,5] 
        i = 1
        j = 3
        msg = "Swap([1,2,3,4,5],1,3) should return [1,4,3,2,5]"
        expected = [1,4,3,2,5]
        result = TestWeek8.STUDENT['Swap'](testval,i,j)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_Lowest(self):
        '''Lowest([1,2,3,4,5] should return 1'''
        testval = [1,2,3,4,5] 
        expected = 1 
        msg = "Lowest([1,2,3,4,5] should return 1"
        result = TestWeek8.STUDENT['Lowest'](testval)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_Lowest2(self):
        '''Lowest([-1,-2,-3,-40,5] should return -40'''
        testval = [-1,-2,-3,-40,5] 
        expected = -40 
        msg = "Lowest([-1,-2,-3,-40,5] should return -40"
        result = TestWeek8.STUDENT['Lowest'](testval)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_OnlyEvens(self):
        '''OnlyEvens([1,2,3,4,5,6] should return [2,4,6]'''
        testval = [1,2,3,4,5,6]
        expected =  [2,4,6]
        msg = "OnlyEvens([1,2,3,4,5,6] should return [2,4,6]"
        result = TestWeek8.STUDENT['OnlyEvens'](testval)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_OnlyEvens2(self):
        '''OnlyEvens([1,3,5] should return []'''
        testval = [1,3,5]
        expected =  []
        msg = "OnlyEvens([1,3,5] should return []"
        result = TestWeek8.STUDENT['OnlyEvens'](testval)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_OverDraft(self):
        '''Overdraft(100,[10,20,30]) should return 40'''
        balance = 100
        transactions = [10,20,30]
        expected = 40 
        msg = "Overdraft(100,[10,20,30]) should return 40"
        result = TestWeek8.STUDENT['Overdraft'](balance,transactions)
        self.assertEqual(result, expected, msg=msg) 

    @weight(1)
    def test_OverDraft2(self):
        '''Overdraft(20,[10,20,30]) should return -10'''
        balance = 20
        transactions = [10,20,30]
        expected = -10 
        msg = "Overdraft(20,[10,20,30]) should return -10"
        result = TestWeek8.STUDENT['Overdraft'](balance,transactions)
        self.assertEqual(result, expected, msg=msg) 