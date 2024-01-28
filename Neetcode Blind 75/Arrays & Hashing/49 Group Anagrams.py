'''
time complexity: O(n) 
space complexity: O(n) - at worst pushing n anagrams hashtable
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]

        res = []
        seen = {}
        # use hashmap to store anagram instances
        for word in strs:
            sort = ''.join(sorted(word))
            if sort not in seen:
                seen[sort] = [word]
            else:
                seen[sort].append(word)

        for val, key in seen.items():
            res.append(key)
        return res
        