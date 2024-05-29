# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        # 0. calculate length of ll
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        # 1. create an array to place nodes in order
        placement = [None] * length
        node = head
        cur_pos = 0
        # 2. place nodes in correct order
        while node:
            ind = (cur_pos + k) % length
            placement[ind] = node
            node = node.next
            cur_pos += 1

        # 3. connect nodes in array
        dummy = ListNode(-1)
        curr = dummy
        for n in placement:
            curr.next = n
            curr = curr.next
        # 4. set last node next to None to prevent cycle
        placement[-1].next = None
        return dummy.next