# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        values = []
        def helper(node):
            if not node:
                values.append("#")
            else:
                # preorder traversal
                values.append(str(node.val))
                helper(node.left)
                helper(node.right)
        helper(root)
        return ' '.join(values)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(values)
            if val == "#":
                return None
            # preorder traversal
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        # creates an iterator object to parse list
        values = iter(data.split())
        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))