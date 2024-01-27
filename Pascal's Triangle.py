class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        
        pascal = [[1]]
        for i in range(1, numRows):
            row = [1]

            for j in range(1, i):
                val = pascal[i-1][j-1] + pascal[i-1][j]
                row.append(val)

            row.append(1)
            pascal.append(row)

        return pascal