#!/bin/python

# Merge pre-sorted arrays of int value, removing duplicates
#

def find_min(*args):
    argc = len(args)
    pos = 0
    minval = None
    for i in range(argc):
        if args[i] == None:
            continue
        elif minval == None or args[i] <= minval:
            minval = args[i]
            pos = i    
    #print (minval, pos)
    return (minval, pos)

def merge_array(a, b, c):
    n = len(a)
    m = len(b)
    p = len(c)
    i, j, k = 0, 0, 0
    out = list()
    while i<n or j<m or k<p:

        if i>=n:
            vi = None
        else:
            vi = a[i]
        if j>=m:
            vj = None
        else:
            vj = b[j]
        if k>=p:
            vk = None
        else:
            vk = c[k]

        (val, pos) = find_min(vi, vj, vk)

        if not val in out:
            out.append(val)
            print out

        if pos==0:
            i +=1
        elif pos==1:
            j +=1
        elif pos==2:
            k +=1

    return out

if __name__ == '__main__':
    A = [-100, -1, 0, 0, 0, 0, 1, 100]
    B = [-90, -1, 0, 0, 0, 1, 10]
    C = [-20, -1, 0, 0, 0, 2, 5]

    D = merge_array(A, B, C)
    print D
