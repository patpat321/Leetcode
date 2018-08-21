"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p == None or q == None:
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            if node1.left != None and node2.left != None:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node1.left == None and node2.left == None:
                pass
            else:
                return False
            if node1.right != None and node2.right != None:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node1.right == None and node2.right == None:
                pass
            else:
                return False
        return True
"""
Traverse through the trees and check each node's presence and value.
"""
