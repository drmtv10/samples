"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position in [0,1]:
        return position
    else:
        fibval = get_fib(position-1) + get_fib(position-2)
        return fibval
    return -1

def get_fib_loop(position):
    if position in [0,1]:
        return position
    first = 0
    second = 1
    fibval = first+second
    for i in range(2,position):
        first = second
        second = fibval
        fibval = first+second
    return fibval

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

for i in range(15):
    print "fib(",i,")=",get_fib(i)
