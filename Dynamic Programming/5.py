"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        longest = s[0]
        for i in range(len(s) - 1):
            odd = self.findlongest(s, i, i)
            even = self.findlongest(s, i, i + 1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest

    def findlongest(self, s, i, j):
        tmp = s[i]
        while s[i] == s[j]:
            tmp = s[i:j + 1]
            if i == 0 or j == len(s) - 1:
                break
            i -= 1
            j += 1
        return tmp
 """
 Start from the current point to calculate the palindromic for odd and even condition. Traverse through the entire string
 to find the palindromic of maximum length.
 """
