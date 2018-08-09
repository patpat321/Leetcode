"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        queue = [[root.left, 2], [root.right, 2]]
        while queue:
            node, depth = queue.pop()
            if node == None:
                continue
            if node != None:
                queue.insert(0,[node.left, depth+1])
                queue.insert(0,[node.right, depth+1])
            if node.left == None and node.right == None:
                return depth
"""
Use queue for breadth-first search
"""
