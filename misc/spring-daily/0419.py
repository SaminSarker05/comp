class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        # 1. hold length and width of land
        m = len(land)
        n = len(land[0])

        def find(i, j):
            # 1. traverse row and col of a farmland to calc total area
            l, w = 0, 0
            lookl, lookw = i+1, j+1
            while lookl < m:
                if land[lookl][j] == 1:
                    l += 1
                else: break # end early if not contiguous
                lookl += 1
            while lookw < n:
                if land[i][lookw] == 1:
                    w +=1
                else: break # end early if not contiguous
                lookw += 1
            # 2. mark area of farmland as forest to not revisit
            for a in range(i, i+l+1):
                for b in range(j, j+w+1):
                    land[a][b] = 0
            # 3. return coordinates of top-left and bottom right corner
            return [i, j, i+l, j+w]
            

        # 4. loop through land and call func when piece of farmland found
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    res.append(find(i, j))
        
        return res
