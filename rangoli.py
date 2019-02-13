"""
You are given an integer, 

. Your task is to print an alphabet rangoli of size 

. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary
has the alphabet letter (in alphabetical order).
Input Format
Only one line of input containing, the size of the rangoli.
Constraints





Output Format
Print the alphabet rangoli in the format explained above.
Sample Input
5
Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string
def print_rangoli(size):
    # your code goes here
    #alphabet="abcdefghijklmnopqrstuvwxyz" = string.ascii_lowercase
    rangoli_width = 2*size - 2 + 2*size - 1
    rangoli_str = string.ascii_lowercase[0:size]
    # top half of the rangoli range(size-1..) + bottom half range(size)!
    for i in range(size-1,0,-1) + range(size):
        rangoli = list()
        for j in range(size-1,i,-1):
            rangoli += rangoli_str[j]
        for j in range(i, size):
            rangoli += rangoli_str[j]
        print ("-".join(rangoli)).center(rangoli_width, '-')
            


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
