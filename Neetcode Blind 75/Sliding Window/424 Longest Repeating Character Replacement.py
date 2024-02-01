class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) == 1:
            return 1


        # keep track of frequency and max count of a letter to calc needed changes
        # if needed changes within k recalc total
        # else slide window and decrease frequency

        l, total = 0, 0
        freq = {}

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1

            length = r - l + 1
            change = length - max(freq.values())
            if change <= k:
                total = max(total, length)
            else:
                
                freq[s[l]] -= 1
                l += 1
        return total