from collections import deque

class Node(object):
  def __init__(self, val, left_child=None, right_child=None):
        self.value = val
        self.left=left_child or None
        self.right=right_child or None

class Bst(object):
  def __init__(self, nodes=[]):
        self.tnodes = nodes or []

  # depth first search
  def inorder_traversal(self, node):
    if node:
        self.inorder_traversal(node.left)
        print "node=", node.value, node.visited
        if node:
            node.visited = True
        print "depth=", self.depth, "node=", node.value, node.visited
        self.inorder_traversal(node.right)
    return None

  def get_bst_depth_breadthFirstSearch(self):
    depth = 0
    bst_q = deque() #Root - level 0
    node = self.tnodes[0] 
    bst_q.append(node)
    while bst_q:
        node = bst_q.pop()
        depth_L = depth_R = 0
        if node.left:
            bst_q.append(node.left)
            depth_L = 1
        if node.right:
            bst_q.append(node.right)
            depth_R = 1
        #print "depth=", depth, "node=", node.value
        depth += (depth_L or depth_R)
    return depth

# --- BST used
#     0 = ROOT
#    /\
#   1  2
#   /\
#  3  4
#     /\
#    5  6
#
nodes = [None for i in range(7)]
nodes[5] = Node(5)
nodes[6] = Node(6)
nodes[4] = Node(4, nodes[5], nodes[6])
nodes[3] = Node(3)
nodes[2] = Node(2)
nodes[1] = Node(1, nodes[3], nodes[4])
nodes[0] = Node(0, nodes[1], nodes[2])
bst = Bst(nodes)
# should be 3
print bst.get_bst_depth_breadthFirstSearch()

              
