# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_in_s = s.count('a')
    print 's=',s, 'a\'s in s=',a_in_s
    num_of_s = int(n / len(s))
    print 'n=',n, 'len(s)=', len(s), 'num_of_s=', num_of_s
    sub_s = n % len(s)
    a_in_sub_s = (s[:sub_s]).count('a')

    total_a_in_nxs = num_of_s * a_in_s + a_in_sub_s
    return total_a_in_nxs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)
    print 'repeatedString=', result
    
    #fptr.write(str(result) + '\n')

    #fptr.close()
