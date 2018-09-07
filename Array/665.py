"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        cnt = 0
        one = nums[:]
        two = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                index = i
        if cnt == 0:
            return True
        elif cnt == 1:
            one[index] = one[index+1]
            two[index+1] = two[index]
            if sorted(one) == one or sorted(two) == two:
                return True
            else:
                return False
        else:
            return False
"""
First, find a pair where the order is wrong. Then there are two possibilities, either the first in the pair can be modified or the second can be modified to create a valid sequence. We simply modify both of them and check for validity of the modified arrays by comparing with the array after sorting.

I find this approach the easiest to reason about and understand.

- Yangshun
"""
