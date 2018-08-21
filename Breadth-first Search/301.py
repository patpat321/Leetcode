"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        check = [s]
        while True:
            res = filter(self.isvalid, check)
            res2 = list(res)
            if res2:
                return res2
            else:
                check = set([k[:i] + k[i+1:] for k in check for i in range(len(k))])
    
    def isvalid(self, s):
        st = list(s)
        stack = []
        for i in range(len(st)):
            if st[i] == '(':
                stack.append(i)
            elif st[i] == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
"""
Use filter() to return the valid string, and modify the string with each loop.
The isvalid() is implemented by DFS to check the pair of parathesis.
"""
