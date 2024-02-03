'''
time complexity: O(n) 
space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        last = None
        while head:
            nexth = head.next
            head.next = last
            last = head
            head = nexth

        return last