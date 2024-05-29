# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 0. recursive solution
        if list1 and list2: # 1. check if both nodes exist
            node = ListNode()
            # 2. compare values and insert smaller
            node.val = list1.val if list1.val <= list2.val else list2.val
            if list1.val <= list2.val: 
                # 3. make recursive call to next nodes
                part = self.mergeTwoLists(list1.next, list2)
            else: 
                part = self.mergeTwoLists(list1, list2.next)
            node.next = part
            return node
        # 4. if only one node or none return one value or None respectively
        if list1: return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        if list2: return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return None