from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False     # edge case
        # a palindrome needs even count of each character and/or one char or only one char

        # to do so the frequency of each char should be divisible by 2; can have at max k odd lengths for each kth string
        store = Counter(s)  # faster build of frequency dict

        odds = 0
        for val in store.values():
            if val % 2 != 0:
                odds += 1

        if odds > k: return False
        return True
