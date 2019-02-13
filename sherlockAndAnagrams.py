# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python

import math
import os
import random
import re
import sys

# anagrams for a word
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


word = "abc"
print list(all_perms(word))

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    """ First, calculate anagrams using permutations, similar to the
    function copied above or using itertools.permutations function -
    https://docs.python.org/2.7/library/itertools.html#itertools.permutations
    Then, need to confirm if any of the entries are duplicates in list and
    remove duplicates, if they are in list (convert to set?)
    Next, go through lists and identify anagrams - track count.
    This is the count that returns number of sub-pairs of a given string that
    are anagrams of each other.
    """

"""
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

     #   fptr.write(str(result) + '\n')

    #fptr.close()
"""
