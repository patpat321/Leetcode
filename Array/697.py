"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for i in range(len(nums)):
            if nums[i] not in cnt:
                cnt[nums[i]] = [i,i,1]
            else:
                cnt[nums[i]][1] = i
                cnt[nums[i]][2] += 1
        maxk, maxv = [], 0
        for k, v in cnt.items():
            if v[2] > maxv:
                maxk = [k]
                maxv = v[2]
            if v[2] == maxv:
                maxk.append(k)
        res = len(nums)
        for j in maxk:
            res = min(res, cnt[j][1] - cnt[j][0])
        return res+1
"""
Store the position when the number first appear and the last appearance, along with the time of the number. 
Find the number with the maximum times, then calculate the shortest distance.
"""
