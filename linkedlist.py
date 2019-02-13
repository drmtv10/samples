"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        cur_pos = 1
        while current:
            #print position, cur_pos, current.value
            if int(cur_pos) == int(position):
                return current
            current = current.next
            cur_pos += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        cur_pos = 1
        current = self.head
        prev = current 
        while current:
            if cur_pos == position:
                if (cur_pos != 1):
                    new_element.next = current
                    current = new_element
                    prev.next = new_element
                else:
                    self.head = new_element
                    new_element.next = current
		break
	    prev = current
            current = current.next
            cur_pos += 1
		
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
	prev = current
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            
    def print_ll(self, log):
        """ debug function to print linked list"""
        current = self.head
        print "Printing Linked list -", log
        while current:
            print current.value, current.next
            current = current.next
        print "-- end of linked list"

        """Add a couple methods to our LinkedList class,
        and use that to implement a Stack.
        You have 4 functions below to fill in:
        insert_first, delete_first, push, and pop.
        Think about this while you're implementing:
        why is it easier to add an "insert_first"
        function than just use "append"?"""

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element
        pass

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head == None:
            return None
        else:
            current = self.head
            self.head = current.next
            return current
        pass

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        current = self.ll.delete_first()
        return current
        pass


# Test cases LinkedList
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

ll.print_ll("after get_position(3)")
# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value
ll.print_ll("after insert(e4,3)")

# Test delete
ll.delete(1)
ll.print_ll("after delete(1)")
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

ll.insert(e1,1)
ll.print_ll("after re-insert(1)")
ll.delete(2)
ll.print_ll("after delete(2)")

# Test cases - STACK
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)
stack.ll.print_ll("linked list creating Stack e1")

# Test stack functionality
stack.push(e2)
stack.ll.print_ll("linked list push e2")
stack.push(e3)
stack.ll.print_ll("linked list after adding e1,e2,e3")
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value
