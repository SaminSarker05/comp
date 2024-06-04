class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []

        # 0. mapping between digits and letters
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        k = len(digits)
        
        # 1. dfs algo to explore all letter combinations
        def dfs(ind, running):
            # 2. if length is met then add to res
            if len(running) == k:
                res.append(running)
                return
            
            # 3. add a letter from the current digit
            for letter in mapping[digits[ind]]:
                # 4. next recursive call must add letter for next digit
                dfs(ind + 1, running + letter)
        dfs(0, "")
        return res