# https://leetcode.com/problems/product-of-array-except-self/
"""
The solution must be computed without using the division operation.

For each position, compute the prefix product of all the elements in the array except itself.
In the reverse order, compute the postfix product of the prefix and the input array element.

Time: O(N)
Space: O(1), where the output array does not count
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        ans = [0] * N
        ans[0] = 1
        
        # prefix product
        for i in range(1, N):
          ans[i] = ans[i-1] * nums[i-1]
        
        # postfix product
        post = 1
        for i in reversed(range(N)):
            ans[i] = post * ans[i]
            post *= nums[i]
        
        return ans
