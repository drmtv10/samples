# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python

import math
import os
import random
import re
import sys
import pprint

# Complete the makeAnagram function below.
def makeAnagram_sort(a, b):
    '''
    Input: string a, b
    Output: num of chars, that should be removed, total from both strings
    such that remainder of a / b string are anagrams of each other
    Algo:
    - Need to find common characters in each string, and count of
    common characters.
    - Remove characters that exist only in a or b.
    - Remove extra characters (previous step might take care of this).
    a = cdeefgh
    b = abccdefff
    1. take smaller of the two string - this is how many chars anagram
    will have.
    2. a is smaller string.  Sort a.
    3. sort b.
    4. Now, a character in a, that is not in b, that should be discarded.
    5. any characters left in b, that are extra, can be discarded.
    '''
    n = len(a)
    m = len(b)
    num_removed = 0
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    i=0
    j=0
    #print a_sorted, b_sorted
    while i < n or j < m:
        print i, j, num_removed
        #print anagram_sorted[i], longer_str[j]
        if i > n - 1:
            num_removed += 1
            j += 1
        elif j > m -1:
            num_removed += 1
            i += 1
        elif a_sorted[i] < b_sorted[j]:
            i += 1
            num_removed += 1
        elif a_sorted[i] > b_sorted[j]:
            j += 1
            num_removed += 1
        else:
            i += 1
            j += 1
    return num_removed

def makeAnagram(a, b):
    '''
    build dict-map for letters, compare - if same, anagrams else
    find non-matching count and characters, which is answer.
    sort based algorithm above is O(n+m) for sort, + O(n+m) for comparing
    characters.  Dict-map is likely to be only O(1), as it's constant time
    to build map (though iterating for n+m characters for counting map).
    cdeefgh
    abccdefff
    '''
    char_map = dict()
    for c in a:
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] +=1
    #print a, b
    #pprint.pprint(char_map)
    for c in b:
        if c not in char_map:
            char_map[c] = -1
        else:
            char_map[c] -= 1
    #print char_map
    char_extra = 0
    for v in char_map.itervalues():
        char_extra += abs(v)
    return char_extra

        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)
    print res

    #fptr.write(str(res) + '\n')

    #fptr.close()
