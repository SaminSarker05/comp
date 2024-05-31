class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i = 0
        # 0. find starting interval to merge with
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            merged.append(intervals[i])
            i += 1
        # 1. merge intervals and update newInterval range
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        # 2. add rest of intervals to result
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged