"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_s = 0
        i, j = 0, len(height)-1
        while i != j:
            wall = min(height[i], height[j])
            dis = j - i
            max_s = max(max_s, wall*dis)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_s
"""
The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. 
Further, the farther the lines, the more will be the area obtained.
We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. 
Futher, we maintain a variable maxareamaxarea to store the maximum area obtained till now. 
At every step, we find out the area formed between them, update maxareamaxarea and move the pointer pointing to the shorter line towards 
the other end by one step.
"""
