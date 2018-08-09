"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        ref = {}
        ref2 = {}
        for i in range(len(s)):
            if s[i] not in ref:
                ref[s[i]] = t[i]
            if ref[s[i]] == t[i]:
                continue
            else:
                return False
        for j in range(len(t)):
            if t[j] not in ref2:
                ref2[t[j]] = s[j]
            if ref2[t[j]] == s[j]:
                continue
            else:
                return False
        for n,v in ref.items():
            if n != ref2[v]:
                return False
        return True
