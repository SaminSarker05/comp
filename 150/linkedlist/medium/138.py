"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # 0. can use hashmaps to instant access to indices
        # mapping between new and old lls
        if not head: return head
        mapping = {}
        curr = head
        while curr:
            # 1. store map between old and new notes
            mapping[curr] = Node(curr.val)
            curr = curr.next
        curr = head # 2. reset marker node
        while curr:
            # 3. average constant time access to each node
            if curr.next:
                mapping[curr].next = mapping[curr.next]
            if curr.random:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next
        return mapping[head]



        # 0. have two lists for easy access to indices of old and new ll
        if not head: return head
        old = []
        storage = []
        root = copy = Node(head.val)
        curr = head.next
        storage.append(copy)
        old.append(head)
        # 1. make a copy of each node and append to arrays
        while curr:
            old.append(curr)
            created = Node(curr.val)
            copy.next = created
            storage.append(created)
            curr = curr.next
            copy = copy.next

        # 2. find the random index of the associated node and point to index in new ll
        again = head
        pos = 0
        while again:
            if again.random:
                ind = old.index(again.random)
                storage[pos].random = storage[ind]
            again = again.next
            pos += 1
        
        return root
