#-*- coding:utf-8 -*-

import sys
import unittest

sys.path.append('..');

from lib import mysort 
from util_test import *

ALL_TESTCASE=list();

class mysort_testCase(unittest.TestCase):
    """ """
    def setUp(self):
        self.data={
            ( 5,2,4,6,1,3 ):[ 1, 2, 3, 4, 5, 6 ],
            (2,4,5,7,1,2,3,6):[1,2,2,3,4,5,6,7],
            (2,8,7,1,3,5,6,4):[1,2,3,4,5,6,7,8]
            };
        print "test data:",self.data;
        #self.data={( 5,2,4,6,1,3 ):[ 1, 2, 3, 4, 5, 6 ],(2,4,5,7,1,2,3,6):[1,2,2,3,4,5,6,7]};
        pass

    def testValue(self):
        #print mysort.ALL
        for _unit in mysort.ALL:
            for (_k,_v) in self.data.items():
                self.assertEqual(_unit(_k) ,_v);
        #self.assertEqual(,);
        pass

    def tearDown(self):
        pass
ALL_TESTCASE.append(mysort_testCase);

if(__name__=="__main__"):
    unittest.main()

