"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums[0]
        maxnum = nums[0]
        for num in nums[1:]:
            if dp > 0:
                dp += num
            else:
                dp = num
            maxnum = max(maxnum, dp)
        return maxnum
"""
Going through the string once, whenever the sum falls below 0, start over from the current number.
Think about the format of the subproblem, use DP to solve it.
"""
