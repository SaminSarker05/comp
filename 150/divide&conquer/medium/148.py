# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 0. collect values of ll in array n
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # 1. sort values of array nlogn
        values.sort()

        # 2. construct new ll using values of sorted array
        curr = dummy = ListNode()
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next


        # CAN ALSO IMEPLEMENT USING MERGE SORT

        # 0. base cases
        if not head or not head.next: return head

        # 1. find middle of a pass in ll using floyd algo
        def find_middle(node):
            slow = node
            fast = node.next
            while fast and fast.next:   
                slow = slow.next
                fast = fast.next.next
            # 2. slow will be at middle when fast and end of ll
            return slow
        
        def merge(left, right):
            # 3. merge two ll using their values
            curr = dummy = ListNode(-1)
            while left and right:
                if left.val <= right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    right = right.next
                curr = curr.next

            # 4. if a ll remains simpy append to end
            if left: curr.next = left
            elif right: curr.next = right

            return dummy.next
        
        mid = find_middle(head)
        # 5. seperate left and right halves of ll
        right_part = mid.next
        mid.next = None

        # 6. make recursive calls and then start merging when at base case
        left = self.sortList(head)
        right = self.sortList(right_part)
        return merge(left, right)
        