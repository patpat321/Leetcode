"""

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum2 = {}
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in sum2:
                    sum2[nums[i] + nums[j]] = [[i,j]]
                else:
                    sum2[nums[i] + nums[j]].append([i,j])
        for m in range(len(nums)):
            for n in range(m+1, len(nums)):
                if target-(nums[m] + nums[n]) in sum2:
                    for i, j in sum2[target-(nums[m] + nums[n])]:
                        if i!=m and i!=n and j!=m and j!=n:
                            if sorted([nums[m], nums[n], nums[i], nums[j]]) not in res:
                                res.append(sorted([nums[m], nums[n], nums[i], nums[j]]))
        return res
