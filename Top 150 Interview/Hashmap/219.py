class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 1. use hashmap to store value and index
        hashmap = {}
        for i in range(len(nums)):
            # 2. if value seen and valid index difference return true
            if nums[i] in hashmap:
                if abs(i-hashmap[nums[i]]) <= k:
                    return True
                # 3. if not valid indexes update to most recent since want to minimize < k
                else: 
                    hashmap[nums[i]] = i
            # 4. if not in map then add 
            else:
                hashmap[nums[i]] = i
        
        return False
            


        