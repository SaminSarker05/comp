class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashMap = defaultdict(int)
        for char in magazine:
            hashMap[char] += 1
        
        for char in ransomNote:
            if char not in hashMap or hashMap[char] <= 0:
                return False
            hashMap[char] -= 1
        
        return True

"""
- make hashmap of characters in magazine
- loop through ransom note 
- if character not in magazine or not enough return false
"""