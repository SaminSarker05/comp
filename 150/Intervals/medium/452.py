class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 0. sort points by first interval value
        points.sort(key = lambda x: x[0])
        res = 1
        # 1. let first end be first balloons end
        end = points[0][1] 

        # 2. loop through points and check if overlap between intervals
        for i in range(1, len(points)):
            s, e = points[i]
            # 3. if no overlap increment res and reset end
            if s > end: 
                res += 1
                end = e
            # 4. if overlap update res as min of ends to guarentee both balloons popping
            else: end = min(end, e)
        return res