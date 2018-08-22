"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[2]+nums[0], nums[1])
        dp = [nums[0], nums[1], nums[2]+nums[0]]
        for i in range(3, len(nums)):
            dp.append(max(dp[i-2], dp[i-3]) + nums[i])
        return max(dp)
"""
Alternatively:

For every house k, there are two options: either to rob it (include this house: i) or not rob it (exclude this house: e).

Include this house:
i = num[k] + e (money of this house + money robbed excluding the previous house)

Exclude this house:
e = max(i, e) (max of money robbed including the previous house or money robbed excluding the previous house)
(note that i and e of the previous step, that's why we use tmp here to store the previous i when calculating e, to make O(1) space)

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pre_i, pre_e = 0, 0
        for money in nums:
            i = pre_e + money
            e = max(pre_i, pre_e)
            pre_i = i
            pre_e = e
        return max(i, e)
"""
