#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    #n = len(prices)
    #for i in xrange(n):
    #    for j in xrange(n-1):
    #        if prices[j] > prices[j+1]:
    #            prices[j], prices[j+1] = prices[j+1], prices[j]
    prices.sort()
    #print prices
    toys = 0
    cost_toys = 0
    while toys < n:
        cost_toys += prices[toys]
        if cost_toys > k:
            break
        else:
            toys += 1
        #print toys, cost_toys, k
    return toys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
