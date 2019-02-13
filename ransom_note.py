# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
# compute time for following loop is O(M x N), where M is
# magazene word count and N is note word count.
# This solution is using Array (list) loop.
# it fails for large test cases with time out failure
# hash based solution needed to reduce run time..
def checkMagazine_list(magazine, note):
    #print note
    #print magazine
    M = len(magazine)
    matched = list()
    for w in note:
        for i in range(M):
            if w == magazine[i]:
                magazine[i] = ''
                break
        #print i, M, magazine
        if i >= M-1:
            print 'No'
            return
    print 'Yes'
    return    
# This should have a runtime of O(M+N)!!
# This turned out to be a successful submission
def checkMagazine_hash(magazine, note):
    #build a dict (hash table) for magazine to get constant time lookup
    M = len(magazine)
    magazine_hashtable = dict()
    for i in range(M):
        if magazine[i] in magazine_hashtable:
            magazine_hashtable[magazine[i]] += 1
        else:
            magazine_hashtable[magazine[i]] = 1
    print magazine_hashtable
    # perform look up via dict, removing entries that already matched
    for w in note:
        if w in magazine_hashtable:
            magazine_hashtable[w] -= 1
            if magazine_hashtable[w] == 0:
                del magazine_hashtable[w]
        else:
            print 'No'
            return
    print 'Yes'
    return    

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine_hash(magazine, note)
