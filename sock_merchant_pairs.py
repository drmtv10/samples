# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs=0
    matched = []
    for i in range(n):
        matched.append(False)

    i=0
    while i<n:
        if matched[i]:
            #print 'matched[',i,']=', matched[i]
            i += 1
            continue
        j = i+1
        while j<n:
            if matched[j]:
                #print 'matched[', j,']=', matched[j]
                j += 1
                continue
            if ar[i] == ar[j]:
                matched[i] = True
                matched[j] = True
                pairs += 1
                #print 'i=', i, 'j=', j, 'pairs=', pairs
                break
            else:
                j += 1
        #print 'i=', i, 'current pairs=', pairs
        i += 1
    return pairs
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
