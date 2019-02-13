#!/bin/python

def lookupIndices(flav1, flav2, cost):
    n = len(cost)
    f2 = 0
    f1 = 0
    print n, cost
    for i in xrange(n):
        print i, cost[i]
        if flav1 == cost[i]:
            f1 = i+1
            print 'got matched', flav1, i, f1
            continue
        if flav2 == cost[i]:
            f2 = i+1
            print 'got matched', flav2, i, f2
            break
        
    print f1, f2
    return

if __name__ == '__main__':
    #cost = [7, 2, 5, 4, 11]
    #flav1 = 7
    #flav2 = 5
    cost = [2, 2, 4, 3]
    flav1 = 2
    flav2 = 2
    lookupIndices(flav1, flav2, cost)
