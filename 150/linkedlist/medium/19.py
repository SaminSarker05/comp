# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node = head
        length = 0
        # 0. calculate length of ll
        while node:
            node = node.next
            length += 1
        # 1. calculate index to remove in forward pass
        toRemove = length - n + 1
        # 2. edge case when first node is to be removed
        if toRemove == 1: return head.next
        pos = 1
        node = head
        # 3. if next node position to be removed then skip 
        while node:
            if pos + 1 == toRemove:
                node.next = node.next.next
                break
            pos += 1
            node = node.next

        return head