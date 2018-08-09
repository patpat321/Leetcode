"""

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = {}
        for i in s:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        for j in t:
            if j not in cnt:
                return False
            else:
                cnt[j] -= 1
        for k,v in cnt.items():
            if v != 0:
                return False
        return True
