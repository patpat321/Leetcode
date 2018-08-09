"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = {}
        string = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in alpha:
                    alpha[s[j]] = 1
                    if j-i+1 > len(string):
                        string = s[i:j+1]
                else:
                    alpha = {}
                    break
        return len(string)
