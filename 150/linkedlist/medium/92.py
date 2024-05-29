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
        for i in range(right-left + 1):
            hold = node.next
            node.next = last
            last = node
            node = hold
        
        prev.next.next = node # 2. node is now the last
        prev.next = last # 3. last is now the first
    
        return dummy.next
        
        
        