class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # sort the given list so we have quick access to the minimum and miaximum from the left and right sides respectively
        # if invalid, we machice choice remove the min or max
        """
        1 2 5
        k = 2
        s = 1
        l = 5

        l / s <= k
        # choose move that brings us closer to <= k
        p, q
        if nums[q] / nums[p + 1] <= nums[q - 1] / nums[p]
            p += 1
        else:
            q += 1
        """

        # can rephrase problem as fiding largest subset where constraints met? sliding window ?
        # sliding window --> finding largest subarray meeting some contrainst
        nums.sort()
        n = len(nums)

        l = 0
        res = n
        for r in range(len(nums)):
            # when do i expand and shrink the window
            # shrink when invalid, grow or advance r while reqiirmeets met

            while nums[r] / nums[l] > k:
                l += 1
            
            res = min(res, n - (r - l + 1))
        
        return res

        # brute force dp tracking l, r positions
        # cache pairs of coordinates in case of reviist

        cache = {}
        # tc: 
        # 6, 19, 33

        if len(nums) <= 1:
            return 0
        
        if len(nums) == 2:
            return 1 if nums[-1] / nums[0] > k else 0

        # n / 2 optios for l
        # n / 2 options for r
        # n^2 dfs + memo algo, total # of unique pairs
        # work per state is constant/neglibible

        def dfs(l, r):
            if not (l < r):
                return float('inf')

            if nums[r] / nums[l] <= k:
                return n - (r - l + 1)

            left = dfs(l + 1, r)
            right = dfs(l, r - 1)
            cache[(l, r)] = min(left, right)

            return cache[(l, r)]
        
        val = dfs(0, n - 1)
        return val if val != float('inf') else n - 1


        l, r = 0, n - 1
        print(nums)

        while l < r:    # terminating condition when pointers equal as we cannot have an empty array
            # check if the constraints are met

            print(nums[l], nums[r])
            if nums[r] / nums[l] <= k:
                break
            if nums[r] / nums[l + 1] <= nums[r - 1] / nums[l]:
                print("yes")
                l += 1
            else:
                print("no")
                r -= 1

            print(l, r)

        twopointers = n - (r - l + 1)

        # also consider just removing mins and maxes

        l, r = 0, n - 1
        while l < r:
            if nums[r] / nums[l] <= k:
                break
            
            l += 1

        choice1 = l
        
        l, r = 0, n - 1
        while l < r:
            if nums[r] / nums[l] <= k:
                break
            
            r -= 1
        
        choice2 = n - r


        return min(twopointers, choice1, choice2)


        



        
