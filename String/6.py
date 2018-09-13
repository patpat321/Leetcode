"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        out = ''
        for i in range(numRows):
            res.append([])
        dir = -1
        point = 0
        for j in range(len(s)):
            if point == 0 or point == numRows-1:
                dir = -1*dir
            res[point].append(s[j])
            point += dir
        for k in range(numRows):
            out += ''.join(res[k])
        return out
"""
Create n(rownumber) lists, then go through the whole string to fill in each corresponding list.
Note when rownumber is 1 should consider otherwise.
"""
