class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums)
        freqlist = defaultdict(int)
        ans = []
        for j in range(k):
            freqlist[nums[j]] += 1

        arr = list(freqlist.keys())
        arr.sort(key=lambda k: (-freqlist[k], -k))
        total = sum([key * freqlist[key] for key in arr[:x]])
        ans.append(total)

        # max heap where key is tuple of frequency and value
        # pop costs logn time complexity with restructure of entire tree
        # lazy update ?


        for i in range(k, len(nums)):
            freqlist[nums[i - k]] -= 1
            freqlist[nums[i]] += 1

            # calculate top x most frequent elements --> needs to be faster ? heap ?
            arr = list(freqlist.keys())
            arr.sort(key=lambda k: (-freqlist[k], -k))
            total = sum([key * freqlist[key] for key in arr[:x]])

            # ans.append(total)
            ans.append(total)

            # ans[i // k] = sum(arr[:x])

        return ans

