class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # calculate the freq of each element in nums
        # find range of possible values for each number
        # one pass because of constraints
        # operation must be performed add 0 to keep unchanged array

        # be greedy in using operations; if available operation and overlaps then use; else reset 
        # [0 1 2        ]
        # [      3 4 5  ]
        # [        4 5 6]

        # line sweep, difference array; range sum
        
        maxfreq = 1

        # sort nums array ? 
        nums.sort()

        curr = nums[0]
        moves = numOperations
        freq = 1

        for i in range(1, len(nums)):
            if nums[i] == curr:
                freq += 1
                maxfreq = max(maxfreq, freq)
                continue

            # try to apply operation if available
            # can expand same number multiple times --> NO
            if moves and nums[i] - (k * moves) <= curr <= nums[i] + (k * moves):
                for i in range(moves):
                    if nums[i] - (k * i) <= curr <= nums[i] + (k * i):
                        moves -= i
                        break
                
                freq += 1
                maxfreq = max(maxfreq, freq)
            else:
                curr = nums[i]
                freq = 1
                moves = numOperations

        return maxfreq





        
