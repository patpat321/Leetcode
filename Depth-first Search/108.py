"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        queue = [nums]
        node = nums[len(nums)//2]
        Root = TreeNode(node)
        nodes = [Root]
        while queue:
            subnums = queue.pop()
            Node = nodes.pop()
            left = subnums[:len(subnums)//2]
            right = subnums[len(subnums)//2+1:]
            if left:
                queue.append(left)
                Node.left = TreeNode(left[len(left)//2])
                nodes.append(Node.left)
            if right:
                queue.append(right)
                Node.right = TreeNode(right[len(right)//2])
                nodes.append(Node.right)
        return Root
"""
Balanced height BST can be built by binary search.
Create two stackes for subset and nodes, then use DFS to traverse through subset and nodes at the same time to build the tree.

Alternatively use recuision:
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        if len(nums)==1:
            root = TreeNode(nums[0])
            return root
        else:
            mid = int(len(nums)//2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[(mid+1):])
            return root
"""
