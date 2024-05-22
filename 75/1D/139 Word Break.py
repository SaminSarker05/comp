class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hold = deque()
        hold.append("")
        seen = set()

        while hold:
            for _ in range(len(hold)):
                curr = hold.popleft()
                if curr == s:
                    return True
                if len(curr) >= len(s):
                    continue
                if curr not in seen:
                    seen.add(curr)

                    for val in wordDict:
                        if val in s and curr + val in s:
                            hold.append(curr + val)

        return False


        