# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 0. recursive solution
        # 1. check if k nodes exists
        node = head
        for _ in range(k):
            if not node: return head
            node = node.next
        
        # 2. reverse ll uing standard method
        last = None
        node = head
        for _ in range(k):
            hold = node.next
            node.next = last
            last = node
            node = hold
        
        # 3. connected k group to recursive call; head now at tail
        head.next = self.reverseKGroup(node, k) # 4. pass in curr which is end of k current k group
        return last