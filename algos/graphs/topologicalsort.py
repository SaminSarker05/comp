"""
- used to sort dependencies of nodes in graph
"""

# DAG - directed acyclic graphs

def topologicalsort(vertices):
  # 0. construct an adj_list to represent graph
  adj_list = collections.defaultdict(list)
  # 1. hold ndegree of each node in a list
  n_degree = [0] * len(vertices)
  for pre, clas in vertices:
    adj_list[pre].append(clas)
    n_degree[clas] += 1
  
  # bfs algo with deque to remove 0 ndegree nodes each iteration
  q = deque()
  for i, val in enumerate(n_degree):
    if val == 0: q.append(i)
  
  array = []

  while q:
    node = q.popleft()
    array.append(node)
    for child in adj_list[node]:
      n_degree[child] -= 1
      if n_degree[child] == 0:
        q.append(child)
  
  # if length of array != len of verticies there was a cycle
  return array
