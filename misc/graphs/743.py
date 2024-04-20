class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        visited = set()
        graph = defaultdict(list)
        q = [(0, k)]

        # 1. adjacency list to represent graph
        for src, t, w in times:
            graph[src].append((t, w))

        # 2. set and heap to apply dijkstra algo
        while q:
            # 3. find min in heap 
            time, node = heapq.heappop(q)
            # 4. if already flaged continue with heap
            if node in visited: continue
            # 5. add node to visited
            visited.add(node)

            # 6. if all nodes visited then time is guarented minimum
            if len(visited) == n:
                return time
            
            # 7. loop through neighbors of node and add to heap
            for neighbor, n_time in graph[node]:
                if neighbor not in visited:
                    # 8. update neighbor time if shorter path found
                    if time + n_time < graph[neighbor]:
                        heapq.heappush(q, (time + n_time, neighbor))

        return -1






        