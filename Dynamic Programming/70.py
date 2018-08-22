"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2]
        if n < 3:
            return dp[n-1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]
"""
The key intuition to solve the problem is that given a number of stairs n, 
if we know the number ways to get to the points [n-1] and [n-2] respectively, 
denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. 
Because from the [n-1] point, we can take one single step to reach [n]. 
And from the [n-2] point, we could take two steps to get there. 
There is NO overlapping between these two solution sets, because we differ in the final step.
"""
