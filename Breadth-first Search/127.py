"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        seen = {beginWord:1}
        wordlist = {i:1 for i in wordList}
        if endWord not in wordList:
            return 0
        while queue:
            word, change = queue.pop()
            if word == endWord:
                return change
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + j + word[i+1:]
                    if (next_word not in seen) and (next_word in wordlist):
                        seen[next_word] = 1
                        queue.insert(0, (next_word, change+1))
        return 0
