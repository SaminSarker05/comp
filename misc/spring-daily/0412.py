class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        # 1. hold frequency of 1 for each column
        heights = [0] * (cols + 1)

        res = 0

        # 2. calculate height of each col at each row
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # 3. use monotonic stack to cut down repeated calculation of min 
            stack = [-1]
            for i in range(len(heights)):
                # 4. if heights[i] < last need to make stack monotonic again
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                
                stack.append(i)
            
        
        return res







        # BRUTE FORCE TO SLOW n^3

        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        # 1. hold frequency of 1 for each column
        heights = [0] * (cols + 1)

        res = 0

        # 2. calculate height of each col at each row
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # 3. generate all contiguous column combinations
            for i in range(len(heights)):
                for j in range(i, len(heights)):
                    # 4. find minumum of this span and multiple by width to get area
                    min_height = min(heights[k] for k in range(i, j + 1))
                    area = min_height * (j-i+1)
                    # 5. update area
                    res = max(res, area)
        
        return res