#!/bin/python

#in-place rotate square matrix by 90 degrees

def rotate90(sq):
    n = len(sq)
    m = len(sq[0])
    print n, m
    if m != n:
        print 'error - not a square matrix'
        return
    # clock-wise 90 rotate
    for i in range(n):
        for j in range(i, m):
            print i, j
            sq[i][j],sq[j][i]=sq[j][i],sq[i][j]
    return

def rotate_anticlockwise90(sq):
    n = len(sq)
    m = len(sq[0])
    #print n, m
    if m != n:
        print 'error - not a square matrix'
        return
    # anti-clock-wise 90 rotate
    # create new matrix (temp local) copy
    sq90 = list()
    for i in range(n):
        sq90.append([0 for j in range(m)])
    #print sq90
    for i in range(n):
        for j in range(m):
            #print i, j
            sq90[j][i] = sq[i][n-1-j]
    print sq90
    print sq
    # make deep copy into original for return
    for i in range(n):
        for j in range(m):
            sq[i][j] = sq90[i][j]
    return

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #rotate90(matrix)
    rotate_anticlockwise90(matrix)
    for r in matrix:
        print r
