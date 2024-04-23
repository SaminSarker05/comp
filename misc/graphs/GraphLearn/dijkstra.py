"""
algo to find shortest path between node and every other node   in directed graph
- edges betwen nodes can have weights or cost
- ElogV runtime
    - E = edges
    - V = vertices/nodes
- use heap and hashset data structure ; every subtree stores min at root
"""

import heapq
"""
methods:
heapq.heapify(LIST)
heapq.heappush(array, val)
heapq.heappop(array)
"""


"""
general steps:
0. set distance between nodes and source as infinity
1. source node has distance 0
2. take min of all nodes (initialy source) and cal distance to other nodes
3. mark source as seen
4. next node of interest is the node with the smallest distance to it from prev

"""

class Node:
  def __init__(self):
    self.d = float("inf") # distance from source
    self.parent = None # holds parent that makes distance to node smallest
    self.finished = False  # flag to mark completion of distance calc

  

def dijkstra(graph, source):
  nodes = {}
  for node in graph:
    nodes[node] = Node()
  
  nodes[source].d = 0
  q = [(0, source)] # queue holds current min distance and node

  while q:
    # we always want to see if we can do better so take route of smallest dist which heap stores effectively for us
    dist, node = heapq.heappop(q) # use heap to get smallest in queue
    if nodes[node].finished:
      continue
    
    nodes[node].finished = True
    # explore all neighbor nodes and calc distances
    for neighbor in graph[node]:
      if nodes[neighbor].finished:
        continue
      new_dist = dist + graph[node][neighbor]
      # if a better distance found than update dist and parent node
      if new_dist < nodes[neighbor].d:
        nodes[neighbor].d = new_dist
        nodes[neighbor].parent = node
        heapq.heappush(q, (new_dist, neighbor))
    
    return nodes


"""
  dijkstra(G, w, s):
  Init(G, s)
  S = nullset
  Q = priority queue
  while Q != nullset:
    u = extractMin(Q)
    S = S u {u}
    for each outgoing edge e of u:
      relax(e)


suppose not. let u be the first vertex u.d > S(s,u)
"""

  