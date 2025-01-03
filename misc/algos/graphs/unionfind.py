"""
- used to group disjoint graphs
"""

# start with disjoint graphs or forest of trees

# at first each node is a root of itself

def unionfind(nodes, vertices):
  forest = [node for node in nodes]
  rank = [0] * len(nodes)  # store height of each tree

  # finds root of a given node
  def find(node):
    if forest[node] != node:
      # path compression -> makes find roots easier by storing results sooner
      forest[node] = find(forest[node])
    
    return forest[node]
  
  def union(n1, n2):
    # find roots of node 1 and 2
    r1, r2 = find(n1), find(n2)

    # make root of one node the root of the other; combining the nodes
    forest[r1] = r2
  

  # optimization for height balanced trees
  def union_rank(n1, n2):
    r1, r2 = find(n1), find(n2)  # find roots of each node

    # get ranks of each tree
    rank1, rank2 = rank[r1], rank[r2]

    # if rank of first node < second node 
    # move node 1 under node 2; add smaller tree to larger tree
    if rank1 < rank2:
      forest[n1] = n2
    elif rank2 < rank1:
      forest[n2] = n1
    else:
      forest[n1] = n2
      rank[n1] += 1  # if same update rank 




