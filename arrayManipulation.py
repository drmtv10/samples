#!/bin/python
# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys
import pprint

# Complete the arrayManipulation function below.
# Default - brute force calculation, this fails for large test case value
def arrayManipulationBrute(n, queries):
    #pprint.pprint(queries)
    #pprint.pprint(n)
    arr = [0 for i in range(n)]
    for q in queries:
        a=q[0]
        b=q[1]
        k=q[2]
        for j in xrange(a-1,b):
            arr[j] += k
        #pprint.pprint(arr) 
            
    max_val =0
    for i in range(n):
        if max_val < arr[i]:
            max_val = arr[i]
    return max_val

def arrayManipulation_1(n, queries):
    #pprint.pprint(queries)
    #pprint.pprint(n)
    arr = [0 for i in range(n)]
    max_val =0
    for q in queries:
        a=q[0]
        b=q[1]
        k=q[2]
        for j in xrange(a-1,b):
            arr[j] += k
            if max_val < arr[j]:
                max_val = arr[j]
        #pprint.pprint(arr) 
            
    #for i in range(n):
    #    if max_val < arr[i]:
    #        max_val = arr[i]
    return max_val

def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        x, y, incr = q
        arr[x-1] += incr
        if((y)<=len(arr)): 
            arr[y] -= incr;
        print(arr)
    max = x = 0
    for i in arr:
       x=x+i;
       #print i, x
       if(max<x): max=x;
    return(max)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
