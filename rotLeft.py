#!/bin/python
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    b = a[0:d]
    n = len(a)
    for i in range(n):
        if i+d < n:
            a[i] = a[i+d]
        else:
            a[i] = b[i+d-n]
    return a

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)
    print(a)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
