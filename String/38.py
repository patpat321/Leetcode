"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cnt = ['1', '11', '21', '1211']
        if n < 5:
            return cnt[n-1]
        for i in range(5, n+1):
            tmp = cnt[-1]
            s = tmp[0]
            c = 1
            out = ''
            for j in tmp[1:]:
                if j == s:
                    c += 1
                else:
                    out += (str(c) + str(s))
                    s = j
                    c = 1
            out += (str(c) + str(s))
            cnt.append(out)
        return cnt[-1]
"""
Calculate the last one using the former one.
"""
