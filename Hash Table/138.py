"""

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        n,m = head, head
        copy = {}
        while n:
            copy[n] = RandomListNode(n.label)
            n = n.next
        while m:
            copy[m].next = copy[m.next] if m.next else None
            copy[m].random = copy[m.random] if m.random else None
            m = m.next
        return copy[head] if head else None
