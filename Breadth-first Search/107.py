"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 1)]
        cnt = {}
        while queue:
            node, depth = queue.pop()
            if not node:
                continue
            if depth not in cnt:
                cnt[depth] = [node.val]
            else:
                cnt[depth] += [node.val]
            queue.insert(0, (node.left, depth+1))
            queue.insert(0, (node.right, depth+1))
        i = 1
        res = []
        while i in cnt.keys():
            res = [cnt[i]] + res
            i += 1
        return res
 """
 Use dictionary to store the depth of the node, then use BFS to go through each layer of the binary tree.
 """
