"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        tmp = []
        teq = 0
        while queue:
            node, level = queue.pop()
            if teq == level:
                tmp.append(node.val)
            else:
                teq = level
                res.append(tmp)
                tmp = [node.val]
            if node.left != None:
                queue.insert(0, (node.left, level+1))
            if node.right != None:
                queue.insert(0, (node.right, level+1))
        res.append(tmp)
        return res
