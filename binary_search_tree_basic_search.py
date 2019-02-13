class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)
        pass

    def bst_insert(self, start, new_val):
        if new_val < start.value:
            if start.left:
                self.bst_insert(start.left, new_val)
            else:
                start.left = Node(new_val)
        else:
            if start.right:
                self.bst_insert(start.right, new_val)
            else:
                start.right = Node(new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif find_val < start.value:
                self.bst_search(start.left, find_val)
            else:
                self.bst_search(start.right, find_val)
        return False
            
    def print_bst(self):
        return self.bst_print(self.root, "")[:-1]

    def bst_print(self, start, traverse):
        if start:
            #print start.value, traverse
            traverse += str(start.value) + "-"
            traverse = self.bst_print(start.left, traverse)
            traverse = self.bst_print(start.right, traverse)
        return traverse
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_bst()
# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
