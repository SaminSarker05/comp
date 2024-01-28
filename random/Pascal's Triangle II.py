class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]

        
        pascal = [[1]]
        for i in range(1, rowIndex+1):
            row = [1]

            for j in range(1, i):
                val = pascal[i-1][j-1] + pascal[i-1][j]
                row.append(val)

            row.append(1)
            pascal.append(row)

        return pascal[rowIndex]
        