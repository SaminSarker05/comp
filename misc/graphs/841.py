class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        # BFS approach
        q = deque() # 0. store room indexes in deque
        q.append(0)
        seen = set()
        res = 0 # hold unique rooms seen

        while q:
            room = q.popleft()
            # 1. if unique room key then update res and process keys in room
            if room not in seen:
                res += 1
                # 2. mark room as seen as to not revisit
                seen.add(room)
                for val in rooms[room]:
                    q.append(val)
        
        # 3. result is true if n unique rooms seen, i.e every room visited
        return res == len(rooms)



        # DFS NAIVE FIRST APPROACH
        keys = [0]
        explored = set()
        
        explored.add(0)
        
        def dfs(room, keys, explored):
            for key in room:
                if key not in keys:
                    keys.append(key)
            if len(keys) == len(rooms):
                return True

            flag = False
            for key in keys: 
                if key not in explored:
                    explored.add(key)
                    flag = flag or dfs(rooms[key], keys, explored)
            
            return flag
        

        return dfs(rooms[0], keys, explored)

