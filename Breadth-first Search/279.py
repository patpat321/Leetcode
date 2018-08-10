"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [[n, 0]]
        lst = [i**2 for i in range(1, n+1) if i**2 <= n]
        seen = set()
        while queue:
            num, step = queue.pop()
            if num == 0:
                return step
            for i in lst:
                if i > num:
                    break
                if num-i not in seen:
                    queue.insert(0, [num - i, step+1])
                    seen.add(num-i)
