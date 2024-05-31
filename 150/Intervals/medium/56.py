class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1: return intervals
        intervals.sort() # 0. sort intervals by ascending order
        res = [intervals[0]]
        # 1. loop through intervals
        for i in range(1, len(intervals)):
            # 2. if current interval start bounded by last interval than overalp exists
            if res[-1][0] <= intervals[i][0] and res[-1][1] >= intervals[i][0]:
                # 3. update last interval in res with new range
                res[-1]=[res[-1][0], max(res[-1][1],intervals[i][1])]
            else: res.append(intervals[i]) # 5. if no overlap add a new interval
        return res