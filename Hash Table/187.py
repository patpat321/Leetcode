"""

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = {}
        res = []
        for i in range(9, len(s)):
            if s[i-9:i+1] not in cnt:
                cnt[s[i-9:i+1]] = 1
            else:
                cnt[s[i-9:i+1]] += 1
        for ind,v in cnt.items():
            if v != 1:
                res.append(ind)
        return res
