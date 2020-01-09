#test.py

import sys
import os

def case1():
    print('case1')

def case2(): 
    print('case2')

def default():
    print('default')

dic = {'case1': case1, 'case2': case2}

dic.get('case11', default)()

