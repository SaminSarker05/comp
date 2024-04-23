"""
graphs can be directed or undirected
contain nodes/vertices and edges that connect nodes
if edge exists between nodes those nodes are adjacent

common ways of representing graph:
- adjacent list: contained linked list of nodes
- adjaceny matrix: 1 representes edge 0 represents no edge
"""


# union-find (graph algorithm)
# nlogn
# data structure: forest of trees


# allows grouping of nodes

# identify membership by representative of each group
# keep track of PARENT of each node
# root of tree/union is representative



"""
323 leetcode
Number of connected components in undirected graph
"""

def solution(n, edges):
  parentslist = [i for i in range(n)]
  rank = [1] * n


  # 1. union:find algorithm
  def find(n):
    curr = n
    # 2. return parent of each provided node
    while curr != parentslist[n]:
      curr = parentslist[curr]
    return curr



