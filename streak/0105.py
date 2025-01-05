class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # difference array
        # prefix sum + line sweep

        # keep a counter or net shift amt for each char in string

        # difference array; fast way to track values in range
        diff_arr = [0 for i in range(len(s))]
        for start, end, direction in shifts:
            amt = (1 if direction == 1 else -1)
            diff_arr[start] += amt
            if end + 1 < len(diff_arr):
                diff_arr[end + 1] -= amt    # negation; to "complete" range
        
        prefix_sum = []
        running = 0
        for i in range(len(diff_arr)):
            running += diff_arr[i]
            prefix_sum.append(running)
        
        res = ""
        for i in range(len(s)):
            if prefix_sum[i] == 0: 
                res += s[i]
                continue
            ch = ord(s[i]) + (prefix_sum[i] % 26) # normalize shift amount

            if ch > 122: ch = chr(ch - 122 + 96)
            elif ch < 97: ch = chr(123 - (97 - ch))
            else: ch = chr(ch)
            res += ch

        return res
