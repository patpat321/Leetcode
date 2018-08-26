"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        imax, imin = res, res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])
            res = max(res, imax)
        return res
"""
The maximum value of sequence ending in current node is either the current node or 
the previous maximum value multiplied by the current positive node or 
the previous minimum value multiplied the current negative node
"""
