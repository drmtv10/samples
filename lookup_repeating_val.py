#Write a function.
#Input: int[]
#Output: A int value from the int[] where the value occurs in the int[] at least (length of array / 4) times.
#Example: [1, 2, 3, 4, 5, 1, 7, 8] => 8/4 = 2, so return a value that occurs at least 2 times, return 1

def lookup_multiple_occurrences(my_arr):
  l = len(my_arr)
  no = l/4
  smy_arr = sorted(my_arr)
  repeated_item =1
  # in sorted array, starting with first item, count how many times current item repeats, and if
  # it repeats more than len/4, then return that item - DONE.
  for i in range(1,l-1):
    if smy_arr[i-1] == smy_arr[i]:
      repeated_item += 1
      if repeated_item >= l/4:
        return smy_arr[i]
    else:
      repeated_item = 1
  return ERROR
