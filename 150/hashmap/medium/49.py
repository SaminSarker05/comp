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

        mapping = defaultdict(list)
        for word in strs:
            find = ''.join(sorted(word))
            mapping[find].append(word)
        
        result = []
        for key, val in mapping.items():
            result.append(val)
        
        return result

"""
- using mapping to store words with sorted order
- store groupings in a hashmap of key list pairs
"""
