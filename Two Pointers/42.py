"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = []
        right = []
        current_l = 0
        current_r = 0
        res = 0
        for i in range(len(height)):
            left.append(current_l)
            if height[i] > current_l:
                current_l = height[i]
        for j in range(len(height)-1, -1, -1):
            right.append(current_r)
            if height[j] > current_r:
                current_r = height[j]
        right.reverse()
        for m in range(len(height)):
            water = min(left[m], right[m]) - height[m]
            if water > 0:
                res += water
        return res
"""
The rain water will only accumulate when the min of 
the highest left wall and highest right wall is larger the height of the wall itself.
Thus we run through the wall to find the highest left wall and the right wall in O(n), and calculate the accumulated water.
"""
