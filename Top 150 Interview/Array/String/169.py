class Solution(object):
    def majorityElement(self, nums):

        # boyer-moore majority voting algo
        # finding majority element that appears more than n/2 times
        votes = 0
        candidate = 0
        for num in nums:
            if votes == 0:
                candidate = num
            
            if candidate == num:
                votes += 1
            else:
                votes -= 1
        return candidate


        n = len(nums)
        # 1. default dict makes new keys = 0
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1
        
        # 2. loop through frequency dict
        pos = n // 2
        for k, v in dic.items():
            # 3. if frequency > n // 2 return key
            if v > pos:
                return k
        
        return 0
