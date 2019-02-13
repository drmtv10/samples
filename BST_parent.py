#!/bin/python
#
# BST given:
#     8
#    / \
#   4   12
#  / \  / \
# 1  7 11 20
#
#
class node(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class myBST(object):
    def __init__(self, root):
        self.root = node(root)
    
    def findMin(self, start):
        if start != None:
            if start.left != None:
                #print 'findMin {}-'.format(start.value)
                self.findMin(start.left)
            else:
                #print 'final findMin {} {}-'.format(start, start.value)
                m = start
                return m

    def findNext(self, start):
        if start:
            if start.left:
                return start.left
            elif start.right:
                return start.right
            else:
                return start.parent

    def printBST(self, start):
        print 'start', start.value, '-'
        # **** This does not work, returned value
        # is NOT a node in tree as python returns a
        # class instance reference that is a shallow copy?
        n = self.findMin(start)
        print '{} {}- left {}'.format(n, n.value, n.left)
        while n:
            n = self.findNext(n)
            print '{}-'.format(n.value)
    
if __name__ == '__main__':
    t_bst = myBST(8)
    t_bst.root.left = node(4)
    t_bst.root.right = node(12)
    t_bst.root.left.left = node(1)
    t_bst.root.left.right = node(7)
    t_bst.root.right.left = node(11)
    t_bst.root.right.right = node(20)
    t_bst.root.right.right.parent = t_bst.root.right
    t_bst.root.right.left.parent = t_bst.root.right
    t_bst.root.left.right.parent = t_bst.root.left
    t_bst.root.left.left.parent = t_bst.root.left
    t_bst.root.left.parent = t_bst.root
    t_bst.root.right.parent = t_bst.root

    t_bst.printBST(t_bst.root)
    
    
    
    
