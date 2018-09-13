"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2]
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            res = 0
            for j in range(1, i+1):
                if dp[i-j] == 0 or dp[j-1] == 0:
                    res += dp[i-j] + dp[j-1]
                else:
                    res += dp[i-j]*dp[j-1]
            dp.append(res)
        return dp[n]
"""
Derive n+1 from n, cause n is the subproblem in n+1.
"""
