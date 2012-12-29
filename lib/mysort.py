#-*- coding:utf-8 -*-

import os
import sys
import re
import traceback
from time import sleep
from datetime import datetime

import logging
import socket
import copy

# Note:  more names are added to __all__ later.
#__all__ = list()
ALL=list()

def insert_sort(arr):
    _arr=list(copy.deepcopy(arr))
    for _i in range(1,len(_arr)):
        #print "_i=",_i
        _key=_arr[_i];

        _j=_i
        #for _j in range(_i,0,-1):
        while(_j>0):
            if(_arr[_j-1]>_key):
                _arr[_j]=_arr[_j-1];
                pass;
            else:
                break
                pass
            _j-=1;
            pass
        _arr[_j]=_key;
        #print _arr
        pass

    return _arr;
    pass
ALL.append(insert_sort);

def t_sort(arr):
    #return [2,32,3];
    #return [1,2,3,4,5,6];
    _arr=list(arr);
    _arr.sort(); 
    return _arr
    pass;
ALL.append(t_sort);

if(__name__=="__main__"):

    a_int=insert_sort(a);

    print "a=",a
    print "a_int=",a_int

    print "Wait for 3 seconds..."
    sleep(3)#停下来看清信息
    #os.system('pause')
