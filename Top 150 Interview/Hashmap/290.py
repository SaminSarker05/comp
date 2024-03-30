class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        # 1. if not same length or same unique values return false
        if len(words) != len(pattern): return False
        if len(set(words)) != len(set(pattern)): return False
        hold = {}
        # 2. map each letter to a word
        for i in range(len(words)):
            if pattern[i] not in hold:
                hold[pattern[i]] = words[i]
            # 3. if letter exists and not equal to current word return false
            elif hold[pattern[i]] != words[i]:
                return False
        
        return True

