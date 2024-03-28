class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 1. divide conquer algorithm
        def divide_conquer(s):
            if len(s) == 0 or k > len(s): return 0

            freq = {}
            # 2. dictionary to store frequency
            for c in s:
                if c not in freq:
                    freq[c] = 0
                freq[c] += 1
            
            for i in range(len(s)):
                # 3. if frequency < k then invalid and split string
                if freq[s[i]] < k:
                    j = i
                    # 4. while loop to find valid splice
                    while j < len(s) and freq[s[j]] < k:
                        j += 1
                    return max(divide_conquer(s[:i]), divide_conquer(s[j:]))
            # 5. if all valid freq then return len of s
            return len(s)

        return divide_conquer(s)


        