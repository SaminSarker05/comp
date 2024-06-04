class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """


        # DP TABULATION
        dp = [False] * (len(s) + 1)

        # 0. each index represents a substring of s
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # 1. if substring exists in dict and prefix then mark as True
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]



        # 0. base case
        if not s: return True
        
        # 1. use deque to hold running solutions
        hold = deque()
        hold.append("")
        seen = set()

        while hold:
            running = hold.popleft()
            # 2. if match then solution was found
            if running == s: return True
            if len(running) >= len(s): continue
            # 3. if substring seen before then ignore
            if running not in seen:
                seen.add(running)
                # 4. loop through dict and append to running string
                for word in wordDict:
                    if word in s and running + word in s:
                        hold.append(running + word)
        
        return False
