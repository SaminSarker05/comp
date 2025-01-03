"""
- rescursive search algo for graph
"""

def dfs(node, target):
  # preorder traversal
  if not node: return False
  if node.val == target: return True
  left = dfs(node.left, target)
  right = dfs(node.right, target)
  
  return left or right

