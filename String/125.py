"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        tmp = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                tmp += s[i].lower()
        if tmp == tmp[::-1]:
            return True
        else:
            return False
