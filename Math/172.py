"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)
 """
 for 5, 2*5, 3*5 they have only one 5
 but for 5*5, 2*5*5 they have two 5
 ...
 so add them all together
 """
