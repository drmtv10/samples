# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    first_hourglass=True
    # sum each hourglass
    for i in xrange(4):
        for j in xrange(4):
            ihourglass_sum = 0
            ihourglass_sum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            ihourglass_sum += arr[i+1][j+1]
            ihourglass_sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            print ihourglass_sum, max_hourglass_sum
            if first_hourglass:
                max_hourglass_sum = ihourglass_sum
                first_hourglass = False
            elif max_hourglass_sum < ihourglass_sum:
                max_hourglass_sum = ihourglass_sum
    return max_hourglass_sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
