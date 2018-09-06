"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for l in range(1, numRows+1):
            tmp = [1]*l
            for i in range(l):
                if i == 0:
                    tmp[i] = 1
                elif i == l-1:
                    tmp[i] = 1
                else:
                    tmp[i] = res[l-2][i-1] + res[l-2][i]
            res.append(tmp)
        return res
"""
Generate it row by row following the rules.
"""
