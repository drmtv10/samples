#!/bin/python
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search



import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavorsBruteForce(cost, money):
    '''
    input: money - total pooled money to spend
    cost - array prices for flavors (not sorted).
    output:
    id 1 and id 2 for two flavors that can be purchased for money.
    Algo:
    Array id printed are 1 based indices.
    If array is sorted, shuffled values result.  Cost for
    flavors can be identified quickly using binary search,
    but then original id in array needs to be looked up, for output.
    Brute force implementation can simply form all possible pairs,
    which would be O(n^2) solution.
    Sort + binary search would be O(2*nlogn).
    '''
    n = len(cost)
    for i in xrange(n):
        for j in xrange(i+1, n):
            if cost[i] + cost[j] == money:
                print i+1, j+1
                return

def lookupIndex(arr, val, excluded=None):
    n = len(arr)
    for i in xrange(n):
        #print i, arr[i]
        if i+1==excluded:
            continue
        if val == arr[i]:
            return i+1

def whatFlavors(cost, money):
    n = len(cost)
    s_cost = sorted(cost)

    # use sorted array & binary search to look up two flavors which can be
    # purchased for given money
    f1 = 0
    found = False
    flav1 = 0
    flav2 = 0
    while not found:
        flav1 = s_cost[f1]
        flav2 = money - flav1
        #print flav1, flav2
        left = f1+1
        right = n-1
        while left <= right:
            #print left, right
            mid = (left + right)/2
            if flav2 == s_cost[mid]:
                found = True
                break
            elif flav2 < s_cost[mid]:
                right = mid-1
            elif flav2 > s_cost[mid]:
                left = mid+1
        f1 += 1

    # look up ID values in original array for both flavors
    # print / return
    #print flav1, flav2
    flavors=list()
    flavors.append(lookupIndex(cost, flav1))
    flavors.append(lookupIndex(cost, flav2, flavors[0]))
    flavors.sort()
    '''
    print n, cost
    for i in xrange(n):
        print i, cost[i]
        if flav1 == cost[i]:
            f1 = i+1
            #print 'got matched', flav1, i, f1
            continue
        if flav2 == cost[i]:
            f2 = i+1
            #print 'got matched', flav2, i, f2
            break
    '''    
    print flavors[0],flavors[1]
    return

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
