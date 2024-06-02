"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 0. hashmap to hold mapping between old and new nodes when revisited
        mapping = {}

        # 1. dfs algo traverse node neighbors
        def dfs(node):
            # 2. if a revisit return the created node to add to neighbors
            if node in mapping:
                return mapping[node]
            # 3. if node not seen create deep copy and add to hashmap
            new_node = Node(node.val)
            mapping[node] = new_node
            # 4. go through neighbors and add to copied node neighbors
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node
        
        return dfs(node) if node else None