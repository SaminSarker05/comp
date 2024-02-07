class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # can sort frequency of each char with hash
        # store in another hash by value
        # order values in a list
        # loop through list and get value from hash

        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        

        byValue = {}
        for k, v in freq.items():
            if v not in byValue:
                byValue[v] = [k]
            else:
                byValue[v].append(k)
        
        res = ""
        
        values = sorted(byValue.keys())
        values.sort(reverse=True)
        for i in values:
            for j in byValue[i]:
                res += i * j
        
        return res