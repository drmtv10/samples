#!/bin/python

import sys
import heapq

# Implemented using heapq - this sorts array and hence is
# O(nlogn +k) solution.
def find_klargest_elements(arr, k):
    n = len(arr)
    if k<=0 or k>n:
        return None
    heapq.heapify(arr)
    return heapq.nlargest(k, arr)

# A solution that does not perform sort, simply linear search
# can be implemented using linear search with O(n*k), where n
# is large and k is small.  For such a scenario, this may be
# preferred to heapq based solution above.
# Without any consideration of trade-off above, I was asked
# to solve this during Pure Storage interview (2/7/2019) and
# did a half-assed job of it.  So, here is the implementation
# for practice.
def insert_maxval(ma, val):
    for j in range(len(ma)):
        if ma[j] < val:
            for k in range(j, len(ma)-1):
                ma[k+1] = ma[k]
            ma[j] = val
            # bail after doing a single assignment
            # this way, maxval array remains sorted with
            # largest value at index 0 and so on..
            return

# Bug - For any duplicates in array, the following returns duplicates!            
def find_klargest_brute(arr, m):
    rval = list()
    n = len(arr)
    # initialize return val with first element (xx - since this
    # results in a bug where if first value is max, all elements are made
    # largest and nothing else gets added)
    # Initializing to lowest int value, in this case -2^31-1
    # python 2.7 int is 32 bit value where as python 3.0 allows very large
    # values, only limited by memory available, so you could put 100-bit
    # int's into regular int variable (which is also the case for py 2.7 long)
    # NO LIMITATION like C/C++ to 64 or 128 bit machine
    for j in range(m):
        rval.append(-sys.maxint-1)
    # populate return values from m max values in array
    for i in xrange(n):
        insert_maxval(rval, arr[i])
    return rval

    
if __name__ == '__main__':
    a = [11,8,4,5,6,6,0,4,10,-1,3,7,2]
    #b = find_klargest_elements(a, 2)
    b = find_klargest_brute(a,4)
    print b
