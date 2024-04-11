class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 0. binary search applicable to sorted arrays variations

        l, r = 0, len(nums) - 1

        # 1. use binary search in sorted portion of graph to search for target
        while l <= r:
    
            mid = (r + l) // 2
            # 2. if middle equal to target return index
            if nums[mid] == target:
                return mid

            # 3. check if left half or right sorted
            if nums[l] <= nums[mid]:
                # 4. check if target in left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # 5. check if target in right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        # 6. if not found return -1
        return -1
