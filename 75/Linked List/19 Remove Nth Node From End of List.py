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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = 0
        cursor = head
        while cursor:
            length += 1
            cursor = cursor.next

        search = length - n
        i = 0
        if i == search:
            return head.next

        cursor = head
        last = None
        while cursor:
            if i == search:
                last.next = cursor.next
                return head
            
            last = cursor
            cursor = cursor.next
            i += 1

        return head
    
