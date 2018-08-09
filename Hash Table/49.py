"""

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        copy = {}
        for word in strs:
            joint = ''.join(sorted(word))
            if joint not in copy:
                copy[joint] = [word]
            else:
                copy[joint].append(word)
        return copy.values()
