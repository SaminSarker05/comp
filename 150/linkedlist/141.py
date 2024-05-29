# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # 0. can use tortoise, hare floyds algorithm to detect cycle
        if not head or not head.next: return False # 1. check that head exists
        h = head.next
        t = head
        # 2. use slow and fast pointers to traverse ll
        while h and h.next:
            # 3. if at any point identical then cycle exists
            if h == t: return True
            t = t.next
            h = h.next.next
        # 4. since fast pointer covers 2x distance a match means repetition of nodes seen
        return False