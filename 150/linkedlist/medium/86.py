# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # 0. can make ll of partitions
        root = lessThan = ListNode(val="#")
        second = other = ListNode(val="#")

        # 1. seperate ll into two ll depending on values
        node = head
        while node:
            if node.val < x:
                lessThan.next = node
                lessThan = lessThan.next
            else:
                other.next = node
                other = other.next
            node = node.next
        # 2. combine the two ll and check if each exists
        if root.next:
            if second.next:
                lessThan.next = second.next
                # 3. make last node.next None to preveny cycle
                other.next = None
                return root.next
            lessThan.next = None
            return root.next
        # 4. again set last node.next to None
        if second.next: other.next = None
        return second.next
        



        # 0. partition nodes into two seperate lists depending on value
        less_than = []
        other = []
        node = head
        while node:
            if node.val < x: less_than.append(node)
            else: other.append(node)
            node = node.next
        
        # 1. attach nodes in order using < first
        root = dummy = ListNode(-1)
        for n in less_than:
            dummy.next = n
            dummy = dummy.next
        
        for j in other:
            dummy.next = j
            dummy = dummy.next

        # 2. set last node.next to None to prevent cycle
        if other: other[-1].next = None
        elif less_than: less_than[-1].next = None
        return root.next