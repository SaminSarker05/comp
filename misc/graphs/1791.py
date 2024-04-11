
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        # 0. each edge must have center node so check which nodes match
        if edges[0][0] == edges[1][0]:
            return edges[0][0]
        elif edges[0][1] == edges[1][0]:
            return edges[0][1]
        elif edges[0][1] == edges[1][1]:
            return edges[0][1]
        elif edges[0][0] == edges[1][1]:
            return edges[0][0]


        # 1. put node in set if repeat then center since only center appears > 1
        seen = set()
        for edge in edges:
            n1, n2 = edge
            if n1 in seen:
                return n1
            if n2 in seen:
                return n2
            seen.add(n1)
            seen.add(n2)
        

        # 2. store each node relation in a hashset see which hashset is greatest
        store = {}
        for edge in edges:
                n1, n2 = edge
                if n1 not in store:
                        store[n1] = []
                if n2 not in store:
                        store[n2] = []  

                store[n1].append(n2)
                store[n2].append(n1)

        for k, v in store.items():
                if len(v) == len(store) - 1:
                        return k

        return 
     
