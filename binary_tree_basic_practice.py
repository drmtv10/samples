class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # iterative algo for non-recursive in-order tree traversal
    def MorrisTraversal(self, start = None):
        if start:
            current = start
        else:
            current = self.root
                
        while current != None:
            if current.left == None:
                print '{}-'.format(current.value)
                current = current.right
            else:
                # find in-order predecessor of current
                pre = current.left
                while(pre.right != None and pre.right != current):
                    pre = pre.right
                # make current as right child of its in-order predecessor
                if pre.right is None:
                    pre.right = current
                    current = current.left
                #revert the changes made in if prt to restore original
                #tree, i.e. fix right child of predecessor
                else:
                    pre.right = None
                    print '{}-'.format(current.value)
                    current = current.right
        

# My implementation below - fixed
# Code mostly copied from solution
class MyBinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return (self.preorder_search(start.left, find_val) or
                    self.preorder_search(start.right, find_val))
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + '-'
            #print traversal
            #if start.left != None:
            traversal = self.preorder_print(start.left, traversal)
                #print traversal
            #if start.right != None:
            traversal = self.preorder_print(start.right, traversal)
                #print traversal
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()

print tree.MorrisTraversal()
