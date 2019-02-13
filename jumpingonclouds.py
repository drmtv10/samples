# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    n = len(c)
    #print 'n=',n
    hops = 0
    i=0
    while i < n-1:
        #print 'c[',i,']=',c[i]
        for j in range(2,0,-1):
            if i+j < n:
                if c[i+j] == 0:
                    i += j
                    hops += 1
                    #print '->c[',i,']=',c[i]
                    break                    
    return hops

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)
    print 'jumpingOnClouds=', result

    #fptr.write(str(result) + '\n')

    #fptr.close()
    
