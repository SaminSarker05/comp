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

        """
        2 solutions:
        - store in array, set next of nodes
        - turtoise hare, reverse, merge
        BOTH O(n)
        """

        arr = []
        curr = head
        # 1. store nodes in array
        while curr:
          arr.append(curr)
          curr = curr.next

        l, r = 0, len(arr) - 1
        last = arr[0]
        # 2. set next of each node to n to last
        while l < r:
          arr[l].next = arr[r]
          arr[r].next = arr[l+1]
          l += 1
          r -= 1
          last = arr[l]
        
        # 3. set last element next to None
        if last:
          last.next = None




        slow = fast = head
        # 1. turtoise hare algo to get to middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse second half
        last = None
        while slow:
            temp = slow.next
            slow.next = last

            last = slow
            slow = temp

        # 3. merge the two lists
        first, second = head, last
        while second.next:
            h1 = first.next
            h2 = second.next

            first.next = second
            second.next = h1

            first = h1
            second = h2