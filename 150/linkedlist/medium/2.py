# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # ALT
        carry = 0
        head = node = ListNode(val="#") # 0. dummy node
        while l1 or l2 or carry: # 1. use carry for sum > 10
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # 2. divmod calculates both quotient and remainder
            carry, t = divmod(v1 + v2 + carry, 10)
            node.next = ListNode(t) # 3. create new node with val sum of l1 l2 nodes
            node = node.next
        return head.next

        
    
        # 0. extract digits from each ll and then add using casting
        n1, n2 = l1, l2
        num1, num2 = "", ""
        while n1 or n2: 
            if n1: 
                num1 += str(n1.val)
                n1 = n1.next
            if n2:
                num2 += str(n2.val)
                n2 = n2.next

        # 1. create new ll using digits of sum
        vals = list(str(int(num1[::-1]) + int(num2[::-1]))[::-1])
        root = ListNode(int(vals[0]))
        node = root
        for i in range(1, len(vals)):
            node.next = ListNode(int(vals[i]))
            node = node.next
        return root