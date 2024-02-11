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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # store linked list in array
        curr = head
        values = []
        while curr:
            values.append(curr)
            curr = curr.next

        left, right = 0, len(values) - 1
        last = values[0]

        # reference nodes using list to specity next
        while left < right:
            values[left].next = values[right]
            values[right].next = values[left + 1]

            left += 1
            right -= 1

            last = values[left]

        if last:
            last.next = None