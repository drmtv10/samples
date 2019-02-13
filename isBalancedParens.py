#!/bin/python
# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    parens = list()
    ret = 'NO'
    for c in s:
        if c in '{[(':
            parens.append(c)
        elif c in ')}]':
            if len(parens) > 0:
                d = parens.pop()
            else:
                return ret
            if c == ')' and d != '(':
                return ret
            elif c == ']' and d != '[':
                return ret
            elif c == '}' and d != '{':
                return ret
    # at end, if parens is not empty, braces did not match up!
    if parens:
        return ret
    else:
        return 'YES'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)
        print result

        #fptr.write(result + '\n')

    #fptr.close()
