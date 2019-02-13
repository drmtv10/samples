"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

#counter=0

def _partition(a, l, r):
    v = a[r]
    i = l
    j = r
    print v, l, r
    while True:
        while (a[i] <= v):
            i += 1
            print 'i=', i
            if i == r:
                break
        while (v <= a[j]):
            j -= 1
            print 'j=', j
            if j == l:
                break
        if i >= j:
            break
        print 'a[i]=', a[i], 'a[j]=', a[j]
        t = a[i]
        a[i] = a[j]
        a[j] = t
    print 'a[r]=', a[r], 'a[i]=', a[i], '_partition returns', i
    a[r] = a[i]
    a[i] = v 
    return i

def _quicksort(array, l, r):
    print '_quicksort a=', array, 'l=', l, 'r=', r
    if r<=l :
        return
    i = _partition(array, l, r)
    _quicksort(array, l, i-1)
    _quicksort(array, i+1, r)

def quicksort(array):
    _quicksort(array, 0, len(array)-1)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
#test = list('asortingexample')
print quicksort(test)
