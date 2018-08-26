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
Space:O(n) Solution, Classic trick to use dictionary to build the connection for linked list.
Space:O(1) Solution, Use two pointers, walker and runner.
walker moves step by step. runner moves two steps at time.
if the Linked List has a cycle walker and runner will meet at some
point.
"""
