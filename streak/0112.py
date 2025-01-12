class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: return False     # edge case
        
        open_bracket = []
        unlocked = []

        # ORDER OF using locked and open brackets matter
        # first exhaust locked open brackets then use unlocked indices to pair remaining if needed
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                open_bracket.append(i)
            else:
                if open_bracket:
                    open_bracket.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while open_bracket and unlocked and open_bracket[-1] < unlocked[-1]:
            open_bracket.pop()
            unlocked.pop()
        
        if open_bracket: return False
        return True
                


        
