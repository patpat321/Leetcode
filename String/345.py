"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set("aeiouAEIOU")
        tmp = ""
        for i in s:
            if i in vowel:
                tmp += i
        tmp = tmp[::-1]
        j = 0
        for i in range(len(s)):
            if s[i] in vowel:
                s = s[:i] + tmp[j] + s[i+1:]
                j += 1
        return s
"""
