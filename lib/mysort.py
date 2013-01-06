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
    """ insert sort
    """

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

def merge(arr,p,q,r):
    """ for merge sort
        arr should be a list
        start from q, end at r-1
    """

    arr1=arr[p:q]
    arr2=arr[q:r]

    arr1.append(1000000);
    arr2.append(1000000);

    i=0;j=0;
    #print "merge(%d,%d,%d): arr1=%s;arr2=%s;"%(p,q,r,arr1,arr2);
    for k in range(p,r):
        if(arr1[i]<=arr2[j]):
            arr[k]=arr1[i];i+=1;
        else:
            arr[k]=arr2[j];j+=1;
        #print "k[%d] in range(%d,%d)= %s;"%(k,p,r,arr);
    #return arr;

    pass;

def _merge_sort(arr,q,r):
    """ merge_sort
        arr should be a list
        start from q, end at r-1
    """
    #merge(arr,p,q,r);

    if(q<r-1):
        mid=(r+q)/2
        #print mid
        _merge_sort(arr,q,mid);
        _merge_sort(arr,mid,r);
        merge(arr,q,mid,r);
        #print "merge(%d,%d,%d)=%s"%(q,mid,r,arr);
    elif(r-1==q):
        merge(arr,q,q,r);
        #print "merge(%d,%d,%d)=%s"%(q,q,r,arr);
    
    #return arr
    return 

def merge_sort(arr):
    """ merge_sort
    """
    _arr=list(arr);
    _merge_sort(_arr,0,len(_arr));
    return _arr
    pass;

ALL.append(merge_sort);

def exchange(arr,i,j):
    temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
    pass;

def partition(arr,q,r):
    _x=arr[r-1];
    i=q-1;
    for j in range(q,r):
        if arr[j]<_x:
            i+=1;
            exchange(arr,i,j);

    exchange(arr,i+1,r-1);

    return i+1;
    pass

def _quick_sort(arr,q,r):
    if (q<r-1):
        p=partition(arr,q,r);
        _quick_sort(arr,q,p);
        _quick_sort(arr,p+1,r);
        pass;
    elif(r-1==q):
        partition(arr,q,r);
    pass;

def quick_sort(arr):
    """ quick sort
    """
    _arr=list(arr);
    _quick_sort(_arr,0,len(_arr));
    return _arr
    pass;

ALL.append(quick_sort);

def t_sort(arr):
    """ just for test
    """
    #return [2,32,3];
    #return [1,2,3,4,5,6];
    _arr=list(arr);
    _arr.sort(); 
    return _arr
    pass;
ALL.append(t_sort);


if(__name__=="__main__"):

    """
    #test for insert_sort
    a_int=insert_sort(a);

    print "a=",a
    print "a_int=",a_int
    """

    """
    #test for merge
    #m=(1,3,5,2,4,6)
    m=[1,3,5,2,4,6,10]
    print "m=",m

    #m_int=merge(m,0,2,len(m))
    m_int=_merge_sort(m,0,len(m))

    print "after merge:"
    print "m=",m
    print "m_int=",m_int
    """

    #"""
    #test for quick sort 
    #m=(1,3,5,2,4,6)
    m=[2,8,7,1,3,5,6,4]
    print "m=",m

    #m_int=partition(m,0,len(m))
    #m_int=_quick_sort(m,0,len(m))
    m_int=quick_sort(m)

    print "after sort:"
    print "m=",m
    print "m_int =",m_int
    print "first partition should be:",[2,1,3,4,7,5,6,8];
    #"""

    print "Wait for 3 seconds..."
    sleep(3)# stop for check
    #os.system('pause')
