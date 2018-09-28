"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        look = {}
        for i in range(len(alpha)):
            look[alpha[i]] = i+1
        res = 0
        s = s[::-1]
        for j in range(len(s)):
            res += look[s[j]]*26**j
        return res
