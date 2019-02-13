#!/bin/python
# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    '''
    input: k - number of important contests to loose
    contests - array 2x2, luck balance for each contest and importance (1/0)
    output: max luck balance
    Algo:
    Find number of important contests that must be won.
    For these important contests, choose ones that have lowest luck balance.
    Sum luck balance saved - luck balance consumed = max luck balance
    '''
    num_of_important_contests = 0
    luck = list()
    luck_bal = 0
    luck_used = 0
    #print contests
    for co in contests:
        #print co[0], co[1]
        if co[1] == 1:
            num_of_important_contests += 1
            luck.append(co[0])
        luck_bal += co[0]
    luck.sort()
    must_win = num_of_important_contests - k
    for i in xrange(must_win):
        #print luck_used
        luck_used += luck[i]
        
    #print luck_bal, luck_used
    luck_bal -= 2*luck_used
    return luck_bal

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)
    print result

    #fptr.write(str(result) + '\n')

    #fptr.close()
