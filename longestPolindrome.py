#!/bin/python

# find longest substring that's a palindrome

class Solution(object):
    ''' runtime for isPalindrome is O(n/2) and longestPalindrome is O(n^2)
    so overall run time is O(n^2 * n/2), which is O(n^3/2) or O(n^3)!!
    '''
    def isPalindrome_bruteforce(self, s):
        n = len(s)
        for i in range(n/2):
            if s[i] != s[n-i-1]:
                return False
        return True
    
    def longestPalindrome_bruteforce(self, s):
        """
        :type s: str
        :rtype: str
        Start with string / substrings of length n-1 down.
        Stop when string / substring is palindrome
        How to find substrings of string:
        for a string with length n,
        substring - n (itself).
        substring n-1 : remove one character at a time, separated by n-1
        chars in-between, basically splitting like below, two sub strings
        abcdef : abcde, bcdef w = n-2, i = 0,1 (s[0:n-1-1], s[1:n-1] => s[i:w+i]
        abcdef : abcd, bcde, cdef w=n-3, i=0,1,2 (s[0:n-2]..
        """
        n = len(s)
        for w in range(n, 0, -1):
            #print w
            for i in range(n-w+1):
                #print i
                subs = s[i:w+i]
                #print subs
                if self.isPalindrome(subs):
                    return subs
        return ""

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        print left, right

        while L >= 0 and R < len(s) and s[L] == s[R]:
            print L, R, s[L]
            L -= 1
            R += 1
            
        print L, R
        return R - L - 1
            
    
    def longestPalindrome(self, s):
        """
        Start with ~P(i,j), where if P(i,j) = true, if Si..Sj is a palindrome
        and false otherwise.
        Therefore, P(i,j) = (P(i+1,j-1) and Si==Sj), where base
        cases for DP solution are:
        P(i,i) = true
        P(i, i+1) = (Si == Si+1)
        This yields a straight forward DP solution where we first initialize
        one and two letters palindromes and work our way up finding
        longest substring palindrome.
        Complexity (TBD time O(n^2) and space O(n^2)
        """
        if len(s) < 1:
            return ""
        start, end, m1, m2, m = 0,0,0,0,0

        for i in range(len(s)):
            m1 = self.expandAroundCenter(s, i, i)
            m2 = self.expandAroundCenter(s, i, i+1)
            m = max(m1, m2)
            if m > end - start:
                start = i - (m-1)/2
                end = i + m/2

        return s[start:end+1]

if __name__ == '__main__':
    obj = Solution()
    teststr = "babad"
    #teststr = "cbbd"
    #teststr = "a"
    #teststr = "geeksforgeeks"
    ans = obj.longestPalindrome(teststr)
    print ans
