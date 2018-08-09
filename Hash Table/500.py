"""

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        one = set('QWERTYUIOPqwertyuiop')
        two = set('ASDFGHJKLasdfghjkl')
        three = set('ZXCVBNMzxcvbnm')
        res = []
        for word in words:
            flag = 0
            if word[0] in one:
                for char in word:
                    if char not in one:
                        flag = 1
                        break
            elif word[0] in two:
                for char in word:
                    if char not in two:
                        flag = 1
                        break
            elif word[0] in three:
                for char in word:
                    if char not in three:
                        flag = 1
                        break
            if flag == 0:
                res.append(word)
        return res
