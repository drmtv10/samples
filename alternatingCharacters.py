# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    '''
    Input - s string.
    Delete repeating characters, such that string only contains
    alternating AB / BA characters. Count and return number of
    repeating characters that need to be deleted to end with a
    string containing alternating characters only
    Output - count of chars to be deleted
    '''
    repeating_char = 0
    for i in xrange(len(s)-1):
        if s[i] == s[i+1]:
            repeating_char += 1
    return repeating_char

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)
        print result

        #fptr.write(str(result) + '\n')

    #fptr.close()
