# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        # 1. store sum as class attribute
        self.sum = 0
    
    def pre(self, node, string):
        # 2. preorder traveral of tree
        if node.left:
            self.pre(node.left, string + str(node.val))
        if node.right:
            self.pre(node.right, string + str(node.val))
        if node.left == None and node.right == None:
            # 3. if both left and right None then add to sum and convert str to int
            self.sum += int(string + str(node.val))

    def sumNumbers(self, root):
        self.pre(root, "")
        # 4. return sum attribute of class
        return self.sum
        