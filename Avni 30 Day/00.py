class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 0. incrementing left pointer can only increase total; decrementing
        # right pointer can only decrease total; given since monotonic

        # Runtime: O(n)

        # 1. two pointers to store left and right positions in array
        l, r = 0, len(numbers) - 1

        # 2. while left is less than right
        while l < r:
            total = numbers[l] + numbers[r]
            # 3. if total greater than target decrement r pointer
            if total > target:
                r -= 1
            # 4. if smaller then increment l pointer
            elif total < target:
                l += 1
            # 5. guarenteed answer
            else:
                return [l+1, r + 1]
        
        return 

        