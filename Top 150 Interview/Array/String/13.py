class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. use hashmap to store equivalents
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        # 2. loop through string
        for i in range(len(s)):
          # 3. if first number smaller than next number subtract first
            if i+1 < len(s) and table[s[i]] < table[s[i+1]]:
                # 4. since next number slso processed subtract first leads to right addition
                res -= table[s[i]]
            else:
                res += table[s[i]]

        return res