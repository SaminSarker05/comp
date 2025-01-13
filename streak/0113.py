from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        # build frequency list of characters in string
        store = defaultdict(int)

        for i in range(len(s)): # only frequency matters since we are returning length
            store[s[i]] += 1

        res = 0

        for char in store:
            if store[char] < 3: res += store[char]
            elif store[char] % 2 == 1: res += 1 # if odd count then only one will remain
            else: res += 2  # if even count then only two will remain; can prove

        return res
        
