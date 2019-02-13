#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# solution using bubble sort times out (22 points)
def minimumBribesBubbleSort(q):
    # Solution:
    # if q[i] - (i+1) > 2 => too chaotic
    # else, re-arrange array back in sorted fashion, using
    # bubble sort (or equivalent) and count number of swaps
    # performed = bribes!
    n = len(q)
    bribes = 0
    swap = False
    #print 'start processing', q
    for i in range(n):
        #print i, q[i], (i+1)
        if q[i] - (i+1) > 2:
            print 'Too chaotic'
            return
    for i in range(n):
        for j in range(n-1):
            if q[j] > q[j+1]:
                swap = True
                bribes += 1
                q[j],q[j+1] = q[j+1],q[j]
        if swap:
            swap = False
        else:
            break
                
    # print q
    print bribes
    return

'''
Copied from discussion.. - a bit fancier version
def minimumBribes(q):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in xrange(0, lastIndex):
        for j in xrange(0, lastIndex):
            comps += 1
            if queue[j] > queue[j+1]:
                temp = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp
                swaps += 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break
    return swaps
'''

### Failed cases 76/77, 202/201, 214/213, 245/244, 


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        #minimumBribes(q)
        minimumBribesBubbleSort(q)
