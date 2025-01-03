"""
- can be used for level order traversal of trees
"""

def bfs(root, target):
  q = deque()
  q.append(root)

  while q:
    for _ in range(len(q)):
      node = q.popleft()
      if node.val == target: return True
      if node.left:
        q.append(node.left)
      
      if node.right:
        q.append(node.right)
  
  return False
  