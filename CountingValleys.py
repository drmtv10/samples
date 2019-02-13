# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    in_valley=False
    valleys=0
    level=0

    for i in range(n):
        if s[i] == 'U':
            level += 1
        elif s[i] == 'D':
            level -= 1
        if level<0:
            in_valley=True
        if in_valley and level == 0:
            valleys += 1
            in_valley=False
    return valleys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)
    print 'Valleys travelled=', result
    
    #fptr.write(str(result) + '\n')

    #fptr.close()
