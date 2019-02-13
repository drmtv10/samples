#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
# this default bubble sort is always O(n**2) run-time
def countSwapsDefault(a):
    n=len(a)
    swap = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                swap += 1
                a[j],a[j+1]=a[j+1],a[j]
    print 'Array is sorted in', swap, 'swaps.'
    print 'First Element:', a[0]
    print 'Last Element:', a[n-1]

# This bubble sort will exit after O(n), if array is mostly
# sorted already, on input.  So, slightly optimized than
# o(n2) solution above.
def countSwaps(a):
    n=len(a)
    swap = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for j in range(n-1):
            if a[j] > a[j+1]:
                isSorted=False
                swap += 1
                a[j],a[j+1]=a[j+1],a[j]
                
    print 'Array is sorted in {} swaps.'.format(swap)
    print 'First Element: {}'.format(a[0])
    print 'Last Element: {}'.format(a[-1])

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
