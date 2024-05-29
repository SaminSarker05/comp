# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 0. ensure ll exists
        if not head or not head.next: return head
        node = head
        # 1. make a list of all duplicate values to remove
        toRemove = set()
        seen = set()
        while node:
            if node.val in seen: toRemove.add(node.val)
            seen.add(node.val)
            node = node.next
        
        # 2. ensure first node is unique
        while head and head.val in toRemove: head = head.next
        curr = head
        # 3. ensure each next node is also unique; skip otherwise
        while curr:
            node = curr.next
            while node and node.val in toRemove:
                node = node.next
                curr.next = node
            curr = curr.next

        return head
        