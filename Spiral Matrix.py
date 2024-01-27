class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())

            if matrix and matrix[0]:
                res +=  matrix.pop()[::-1]

            if matrix and matrix[0]:
                for j in matrix[::-1]:
                    res.append(j.pop(0))
        
        return res