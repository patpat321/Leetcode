"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def str2bin(s):
            res = 0
            q = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == '1':
                    res += 2 ** q
                q += 1
            return res

        def bin2str(num):
            if num == 0:
                return '0'
            res = ''
            while num != 0:
                res += str(num % 2)
                num = num // 2
            return res[::-1]

        return bin2str(str2bin(a) + str2bin(b))
"""
Write the function to covert between string and binary.
int("1100", 2)
bin(12) = '0b1100'
"""
