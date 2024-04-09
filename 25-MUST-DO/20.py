class Solution(object):
    def lengthOfLongestSubstring(self, s):

        l = res = 0
        hold = {}

        # 1. sliding window with optimization
        for r in range(len(s)):
            # 2. if repeating change left pointer to rightmost of repeating
            if s[r] in hold:
                l = max(l, hold[s[r]] + 1)
            hold[s[r]] = r
            # 3. update length of subarray with unique values
            res = max(res, r-l+1)
        
        return res


        l = 0 = res
        running = ""
        hold = {}

        # 1. sliding window
        for r in range(len(s)):
            # 2. add char to sliding window
            running += s[r]
            # 3. if repeating then decrement from left until valid
            while s[r] in hold:
                # 4. update res each time as length of subarray
                res = max(res, r-l)
                hold[s[l]] -= 1
                # 5. update hash table
                if hold[s[l]] == 0:
                    del hold[s[l]]
                l += 1
            # 6. when guarenteed unique add to hash table
            hold[s[r]] = 1
            
        # 7. final compare with hash table length
        res = max(res, len(hold))

        return res