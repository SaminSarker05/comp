class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 1. store freq of t and s in seperate dicts
        store = {i:0 for i in s}
        target = {}
        for i in t:
            if i not in target:
                target[i] = 0
            target[i] += 1
        need = len(target)

        r = 0
        l = 0
        res = [-1, 0, 0]
        # 2. sliding window technique
        while r < len(s):
            # 3. update freq depending on current char
            store[s[r]] += 1
            # 4. if freq meet for target decrement need
            if s[r] in target and store[s[r]] == target[s[r]]:
                need -= 1
            
            # 5. if all char in t in s shift left pointer 
            while l <= r and need == 0:
                char = s[l]
                store[char] -= 1
                # 6. shift left pointer and decrement in store
                if char in target and store[char] < target[char]:
                    need += 1

                # 7. recalculate res by storing r and l if len < prev
                if res[0] == -1 or r - l + 1 < res[0]:
                    res[0] = r - l + 1
                    res[1] = r
                    res[2] = l
                
                l += 1
            
            r += 1

        # 8. return empty string if no sol or splice of answer
        return "" if res[0] == -1 else s[res[2] : res[1] + 1]


