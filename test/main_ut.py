#-*- coding:utf-8 -*-

import sys
import unittest

sys.path.append('../lib');
sys.path.append('../conf');

import mysort_ut
"""
from dt_comm_logAna_ut import Dt_comm_logAna 
from ds_bottom_logAna_ut import Ds_bottom_logAna 
from ds_top_logAna_ut import Ds_top_logAna 
from as_logAna_ut import As_logAna 
from all_conf_logAna_ut import serverName,portSocket
"""
  
#create test collection  
def get_suite():  
    listSuites = [];
    listClass=[];
    listClass.extend(mysort_ut.ALL_TESTCASE);
    #listClass = [mysort_testCase];#, Show_LogAna_testCase];
    #listClass = [LogAna_testCase, SqlSocket_LogAna_testCase, Show_LogAna_testCase];
    for c in listClass:
        listSuites.append(unittest.TestLoader().loadTestsFromTestCase(c));  

    alltests = unittest.TestSuite(listSuites);
    #tests = ['test_result', 'test_sql']
    #oSuite = unittest.TestSuite(map(SqlSocket_LogAna_testCase,tests));
    
    return alltests;     


if(__name__=="__main__"):
    # it's ok for the 2 below method
    #unittest.main(verbosity=2,defaultTest = 'get_suite');
    unittest.TextTestRunner(verbosity=2).run(get_suite());

