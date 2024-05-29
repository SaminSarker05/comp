# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        # 0. use hashset to track seen nodes
        node = head
        while node:
            # 1. if node seen previously then node marks start of cycle
            if node in seen: return node
            # 2. increment over ll by seting node to its next
            seen.add(node)
            node = node.next
        return None