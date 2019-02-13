#!/usr/bin/python
# simple palindrome test
def isPalindrome(teststr):
  l = len(teststr)
  for i in range(l/2):
    #print "i=", i, teststr[i], teststr[l-i-1]
    if teststr[i].lower() != teststr[l-1-i].lower():
      return False
  return True

def main():
    word_b4 = ['Otto', 'Nurses run', 'Apple', 'Oracle']
    for i in range(len(word_b4)):
      print word_b4[i], "is a Palindrome =", isPalindrome(word_b4[i]) 

if __name__ == "__main__":
   main()

