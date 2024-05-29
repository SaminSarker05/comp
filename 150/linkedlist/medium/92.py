# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right: return head
        
        # 0. create dummy node and use var to track previous node from left
        dummy = ListNode(val=-1)
        dummy.next = head
        prev = dummy
        for i in range(left - 1): prev = prev.next

        last = None
        node = prev.next
        # 1. reverse order of nodes left to right
        for i in range(right-left):
            hold = node.next
            node.next = hold.next
            hold.next = prev.next
            prev.next = hold
    
        return dummy.next
        