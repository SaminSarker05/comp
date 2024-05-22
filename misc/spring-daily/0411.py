class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]
        water = 0

        # 1. two pointer solution
        while left < right:
            # 2. store left and right most max at each positions
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            # 3. use minimum of each left and right max
            if lmax <= rmax:
                # 4. water level is minumum of maxes - height at position
                water += lmax - height[left]
                left += 1
            else:
                water += rmax - height[right]
                right -= 1
        
        return water
