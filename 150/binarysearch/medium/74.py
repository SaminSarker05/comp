class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # 0. binary search algo HINT from time complexity

        # 1. identify which row target could be in
        row = -1
        for i in range(len(matrix)):
            if target <= matrix[i][-1]: 
                row = i
                break
        
        # 2. if a row was never found return False
        if row == -1: return False
        
        # 3. perform binary search algo on row
        arr = matrix[row]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target: return True
            if target < arr[mid]:
                right = mid - 1
            else: left = mid + 1
        # 4. if target never found return False
        return False