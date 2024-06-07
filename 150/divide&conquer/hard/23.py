# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # 0. recursive divide conquer algo with mergesort algo
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        # 1. split lists at middle
        mid = len(lists) // 2

        # 2. make recursibe calls with left and right halves
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # 3. return merged result
        return self.merge(left, right)
    
    def merge(self, left, right):
        # 4. combine two ll halves; distinct so dont need to disconnect
        curr = start = ListNode(-1)
        while left and right:
            if left.val <= right.val:
                curr.next = ListNode(left.val)
                left = left.next
            else: 
                curr.next = ListNode(right.val)
                right = right.next
            curr = curr.next
        # 5. append any remaining ll
        curr.next = left or right

        # 6. return result
        return start.next