"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
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
                res.append(tmp.pop())
                teq = level
                tmp = [node.val]
            if node.left:
                queue.insert(0, (node.left, level+1))
            if node.right:
                queue.insert(0, (node.right, level+1))
        res.append(tmp.pop())
        return res
"""
Search the tree using BFS, and then pop the last element in each level.
"""
