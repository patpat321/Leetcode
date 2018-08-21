"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if abs(self.checkdepth(node.left) - self.checkdepth(node.right)) < 2:
                pass
            else:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
        
    def checkdepth(self, node):
        if not node:
            return 0
        stack = [(node, 1)]
        depth = 1
        while stack:
            point, level = stack.pop()
            if point.left:
                stack.append((point.left, level+1))
            if point.right:
                stack.append((point.right, level+1))
            depth = max(depth, level)
        return depth
 """
 Traverse each node in the tree, and check the depth of two subtrees to see if its height balanced.
 """
