#!/bin/python

class Solution(object):
    def ignoredups(self, res, a, b, c):
        #print a,b,c
        if a==0 and b==0 and c==0:
            if not [0,0,0] in res:
                res.append([0,0,0])
                return
        for t in res:
            if (a in t) and (b in t) and (c in t):
                #print a,b,c,t
                return
        # if drop here, means we do not have this triplet yet.
        res.append([a,b,c])
        return
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given an array nums of n integers, are there elements a, b, c
        in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.
        Brute force algo - possibly O(n^3) Or more accurately O(n(n-1)(n-2))
        pick first element - a - i
        pick second element b - j
        Iterate through rest of the array elements for c - k, save i,j,k if a+b+c=0
        This iterates k = j+1 to n
        Iterate a different possible value of b?
        Start:
        Input - [-1, 0, 1, 2, -1, -4]
        i=0, j=1, k= 2..N=6 (-1, 0, 1), (-1,0,2)X, (-1,0,-1)X, (-1,0,-4)X
        i=0, j=2, k= 3..N (-1,1,2)X, (-1,1,-1)X, (-1,1,-4)X
        i=0, j=3, k= 4..N (-1,2,-1), (-1,2,-4)X
        i=0, j=4, k= 5-N (-1,-1,-4)X
        i=1, j=2, k= 3-N (0, 1, 2)X, (0,1,-1)Dup, (0,1,-4)X

        Brute force algo required quite a bit of work to remove dup
        items from result.  As implemented, though, it runs with O(n^3) and
        fails time limit!!

        Improved algo:
        sort input array nums.
        Use sorted array to perform iterations, skipping over duplicates and only
        finding unique triplets that satisfy condition.
        
        """
        N = len(nums)
        res = list()
        for i in xrange(N):
            for j in xrange(i+1, N):
                for k in xrange(j+1, N):
                    if nums[i]+nums[j]+nums[k] == 0:
                        self.ignoredups(res, nums[i], nums[j], nums[k])
        return res

if __name__ == '__main__':
    sum3 = Solution()
    #arr = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    #arr = [0,0,0,0]
    arr = [-2,-2,0,-5,-1,-3,0,4,3,4,1,3,0,-1,0,3]
    ans = sum3.threeSum(arr)
    print ans
    
