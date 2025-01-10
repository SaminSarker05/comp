class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # can go through each string in words2 and build a dict of all chars and their frequencies needed
        need = {}
        for string in words2:
            temp = {}
            for char in string:
                if char not in temp:
                    temp[char] = 0
                temp[char] += 1
            
            for letter in temp:
                if letter in need:
                    # if char already exists then maximimize amount needed so all strings guarenteed subsets
                    need[letter] = max(need[letter], temp[letter])
                else:
                    need[letter] = temp[letter]
        
        res = []

        # for each word; build a dictionary and then check that all strings from list2 are meet
        for string in words1:
            temp = {}
            for char in string:
                if char not in temp:
                    temp[char] = 0
                temp[char] += 1
            flag = True
            for char in need:
                if char not in temp or temp[char] < need[char]:
                    flag = False
                    break
            
            if flag:
                res.append(string)
            
        return res
