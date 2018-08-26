"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = {}
        node = head
        while node:
            if node in seen:
                return True
            seen[node] = 1
            node = node.next
        return False
"""
Classic trick to use dictionary to build the connection for linked list.
"""
