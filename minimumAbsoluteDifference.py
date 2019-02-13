#!/bin/python
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import math
import os
import random
import re
import sys
from operator import methodcaller

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifferenceBruteForce(arr):
    '''
    array with n elements will have n**2 possible pairs.
    task is to find min abs diff between all pairs.
    default brute force algo will take o(n * (n-1)) or O(n**2)
    '''
    n = len(arr)
    min_abs_diff = abs(arr[0]-arr[1])
    for i in xrange(n):
        for j in xrange(i+1, n):
            if abs(arr[i] - arr[j]) < min_abs_diff:
                min_abs_diff = abs(arr[i] - arr[j])
    return min_abs_diff

def minimumAbsoluteDifference(arr):
    '''
    array with n elements will have n**2 possible pairs.
    task is to find min abs diff between all pairs.
    default brute force algo will take o(n * (n-1)) or O(n**2)
    Using sort first - which is O(nlogn) and
    then consecutive diff computation in single loop gives
    answer.  So overall, O(nlogn+n) ~ O(n*logn), better than
    O(n^2), i guess.
    '''
    arr.sort()
    n = len(arr)
    min_abs_diff = abs(arr[0] - arr[1])
    for i in xrange(1, n-1):
        if min_abs_diff > abs(arr[i]-arr[i+1]):
            min_abs_diff = abs(arr[i]-arr[i+1])
    return min_abs_diff                
            
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minimumAbsoluteDifference(arr)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
