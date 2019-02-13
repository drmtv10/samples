#   Given values of two nodes in a Binary Search Tree, write a program to
# find the Lowest Common Ancestor (LCA). You may assume that both the values
# exist in the tree. 
   
#          20
#          /\
#         /  \
#        8    22
#        /\
#       /  \
#      4   12
#          /\
#         /  \ 
#        10   14
        
#            (10,14)= 12  4,14= 8

#class graph_bst(object):
#    __init__(self, nodes=[], edges=[])

# -- OR -- one possible, matrix representation:
graph_bst = [[20,0,0,0,0,0,0,0],
             [8,22,0,0,0,0,0,0],
             [4,12,0,0,0,0,0,0],
             [0,0,10,14,0,0,0,0]]
gbst_rows = 4
gbst_cols = 8

def get_parent(row, col):
    # TODO: add error check to make sure row, col
    # fit into initialized graph_bst matrix
    return graph_bst[int(row)-1][int(col)/2]

def get_pos(val):
    for row in range(gbst_rows):
        for col in range(gbst_cols):
            if val == graph_bst[row][col]:
                #print val, row, col
                return (row,col)
    return None

def get_parentlist(val):
    ret = []
    done = False
    next_val = val
    #print "get_parenlist(", val, ")"
    while not done:
        (row, col) = get_pos(next_val)
        if row>0:
            #print row,col
            next_val = get_parent(row,col)
            ret.append(next_val)
        else:
            done = True
    #print "return", ret
    return ret

def search_LCA(val1, val2):
  p_val1 = get_parentlist(val1)
  #print p_val1
  p_val2 = get_parentlist(val2)
  #print p_val2
    
  for i in range(len(p_val1)):
      for j in range(len(p_val2)):
          if p_val1[i] == p_val2[j]:
              lca = p_val1[i]
              return lca
  return None
                       
# get parent node list for val1
# get parent node list for val2
# 10 = parent nodes list [12, 8, 20]
# 14 = parent nodes list [12, 8, 20]
# comparing parent nodes list, first matching node is [0] = 12 - LCA

# 4,14 - parent nodes list [8,20], [12,8,20] = first matching parent node is 8 - LCA

def main():
    """
    uses graph_bst, a binary search tree with problem defined above
    and finds lowest comman ancestor, given two values (see comment
    at the beginning of file)
    """
    #print "graph binrary search", graph_bst
    print search_LCA(10,14)
    print search_LCA(4,14)


if __name__ == '__main__':
    main()

