"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        for index,value in enumerate(cnt):
            if cnt[value] == 1:
                return value
        return None
