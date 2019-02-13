#!/bin/python
# basic bubble sort

# Basic (bubble) sort takes O(n*(n-1)), which is O(n**2) run-time

#while this bubble sort implmentation bubbles lower values to the front
# and does succeed at sorting, it ties up loops i / j tightly and makes
# it harder to watch progress.  
def bubble_sort(arr):
    n = len(arr)
    #print 'sorting', arr
    for i in range(n):
        for j in range(i+1,n):
            #print i, j, 'current arr=', arr
            if arr[j] < arr[i]:
                #print 'swap', arr[j], arr[i]
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return
# Default bubble sort implementation uses inner
# loop that compares j/j+1 array elements
# and performs swaps.
def bubble_sort(arr):
    n = len(arr)
    #print 'sorting', arr
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                #print 'swap', arr[j], arr[i]
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    return

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        bubble_sort(q)
        print q
    
    #arr = [5, 4, 3, 2, 1, 0]
    #bubble_sort(arr)
    #print arr
