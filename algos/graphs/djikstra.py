"""
- can find shorted path to other nodes form a source in graph
- weights must be nonnegative
"""

def djikstra(vertices, source):
  adj_list = defaultdict(list)
  # adj_list to represent graph
  for n1, n2 in vertices:
    adj_list[n1].append(n2)

  # distance from each node at first infinity except source

  distances = {node:float("inf") for node in adj_list}
  distances[source] = 0

  seen = set()  # keep tracked of visited nodes

  # use bfs and heap to process nodes in tree
  q = []
  q.append((0, source))

  while q:
    # get current dist and node in heap
    dist, node = heapq.heappop(q)
    if node in seen: continue  # ignore if already seen
    seen.add(node)

    # calculate next possible dist to child nodes
    for neighbor in adj_list[node]:
      new_dist = dist + distances[neighbor]
      if new_dist < distances[neighbor]:
        distnaces[neighbor] = new_dist
        heapq.heappush((new_dist, neighbor))
    

