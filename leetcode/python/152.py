# https://leetcode.com/problems/maximum-product-subarray/
"""
The solution entails computing the product in both directions.
Since 0 refreshes all product to itself (i.e. 0), reset to a unit product(i.e. 1)
Get the maximum product from both direction, and return as result
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return nums[0]

        # multiply from both directions
        max_prod = float('-inf')
        forward, backward = 1, 1

        for i in range(N):
            if forward == 0:
                forward = 1
            if backward == 0:
                backward = 1

            forward *= nums[i]
            backward *= nums[N-i-1]

            max_prod = max(max_prod, forward, backward)

        return max_prod
