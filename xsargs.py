#!/bin/python
import sys
import os

if __name__ == '__main__':
    while True:
        teststr = raw_input()
        #print teststr
        if teststr:
            os.system(teststr)
        else:
            break
        
    
