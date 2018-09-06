"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
                if cnt[num] > len(nums)/2:
                    return num
        return num
"""
O(n), run through the list and record the time that number appeared.
Alternatively:
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[(int) (len(nums) / 2)]
"""
