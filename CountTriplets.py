#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets_array(arr, r):
    # iterate through array to build a dict containing triplets,
    # where each triplet represents elements that form geometric
    # progression.
    # arr is len(arr) elements and start with
    # iterating via first 2 elements i,j,
    # where a[0]*r = a[1] and a[1]*r = a[2].
    # Once a[0]*r = a[j] is found, continue until a[j]*r = a[k] is found
    # This is first i=0, j, k triplet.
    # Next, repeat process for i=1, at any point if k = len(arr) then
    # no more triplets
    # This performs O((m-2)**3), so run time is O(n**3).
    # run time needs optimization using hash map - above is brute force
    triplets = 0
    m = len(arr)
    for i in range(m-2):
        for j in range(i+1,m-1):
            if arr[i]*r == arr[j]:
                for k in range(j+1,m):
                    if arr[j]*r == arr[k]:
                        triplets += 1
    return triplets

# this is "working" but takes too long, fails for a few test cases due to that
# reason..
def countTriplets_timeout(arr, r):
    gp = dict()
    # iterate through array, devide each element by r.
    # this builds up dict as gp[a*r**0] = [i..i] , where i is index of
    # first element of triplet i,j,k
    # and gp[a*r**1] = [j..j]
    # and gp[a*r**2] = [k..k]
    # re-arranging array into dict run-time is k * m, where k is value such
    # that r ** k > all elements in arr.
    m = len(arr)
    k = arr[0]
    for i in range(m):
        if r != 1:
            while arr[i] > k:
                k *= r
            while arr[i] < k:
                k /= r
        if not k in gp:
            gp[k] = list()
        if k == arr[i]:
            gp[k].append(i)
    print gp, k        

    triplets = 0
    # special case when r=1
    if r == 1:
        for k,v in gp.iteritems():
            # calculate combinations of v items into groups of 3
            triplets = len(v) * (len(v)-1) * (len(v)-2) / 6 # P(v-items)/3!            
        return triplets
  
    ks = sorted(gp.keys())
    if len(ks) < 3:
        return 0
    print ks

    # run-time for this loop, which counts all triplets, needs
    # to iterate through 3 pairs of keys out of all keys, which is expensive
    # if keys were sorted and each items array was sorted, would it be
    # possible to calculate triplets using a formulae instead of iteration?

    for a in range(len(ks)-2):
        i = ks[a]
        j = ks[a+1]
        k = ks[a+2]
        print i, j, k
        #triplets += len(gp[i]) * len(gp[j]) * len(gp[k])
        for k_i in gp[i]:
            for k_j in gp[j]:
                for k_k in gp[k]:
                    if k_i < k_j and k_i < k_k and k_j < k_k:
                        triplets += 1
                        print '(', k_i, k_j, k_k, ')=(', arr[k_i], arr[k_j], arr[k_k], ')'        
    return triplets            

def countTriplets(arr, r):
    # https://www.hackerrank.com/challenges/count-triplets-1/forum/comments/468507
    # initialize the dictionaries
    r2 = {}
    r3 = {}
    count = 0

    # loop throgh the arr itens
    for k in arr:
        
        # if k in r3 indicates the triplet already completed,
        # the count need be incremented
        if k in r3:
            count += r3[k]

        # if k in r2, it is the secound number of the triplet,
        # your successor (third element k*r) need be added or incremented in the r3 dict
        # because is a potencial triplet 
        if k in r2:
            if k*r in r3:
                r3[k*r] += r2[k]
            else:
                r3[k*r] = r2[k]

        # else, k is the first element of the triplet, so,
        # your seccessor (secound element k*r) need be added or incremented in the r2 dict
        # because is a potencial triplet
        if k*r in r2:
            r2[k*r] += 1
        else:
            r2[k*r] = 1

    return count
"""        
def countTriplets(arr, r):
        # initialize the dictionaries
        r2 = {}
        r3 = {}
        count = 0

        # loop throgh the arr itens
        for k in arr:
                # if k in r3 indicates the triplet already completed,
                # the count need be incremented
                if k in r3:
                        count += r3[k]

                # if k in r2, it is the secound number of the triplet,
                # your successor (third element k*r) need be added or incremented in the r3 dict
                # because is a potencial triplet 
                if k in r2:
                        if k*r in r3:
                                r3[k*r] += r2[k]
                        else:
                                r3[k*r] = r2[k]

                # else, k is the first element of the triplet, so,
                # your seccessor (secound element k*r) need be added or incremented in the r2 dict
                # because is a potencial triplet
                if k*r in r2:
                        r2[k*r] += 1
                else:
                        r2[k*r] = 1

        return count        
"""            
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    print ans
    #fptr.write(str(ans) + '\n')

    #fptr.close()

"""
Testcase # 2:
100 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""

