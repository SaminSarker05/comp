class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 0. sort heights to have expcted array
        expected = sorted(heights)

        res = 0
        # 1. loop through array of students
        for i in range(len(heights)):
            # 2. if actual height != exptected increment res
            if heights[i] != expected[i]: res += 1
        
        return res
