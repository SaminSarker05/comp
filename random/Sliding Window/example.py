# fixed size sliding window
# find largest subarray sum of size K
def findMaxSubarray(array, k):
  res = sum(array[:k])
  running = res

  for r in range(k, len(array)):
    running += array[r]
    running -= array[r-k]

    res = max(res, running)

  return res


# dynamic sliding window
# find minimum subarray with sum >= K
def smallestSubarray(array, target):
  l = 0
  res = float("inf")
  running = 0
  for r in range(len(array)):
    running += array[r]
    while running >= target:
      res = min(res, r-l+1)
      running -= array[l]
      l += 1
  return res


from collections import defaultdict

# dynamic sliding window
# use of hash table
def longestwithKdistinct(array, k):
  res = 0
  track = defaultdict(int)
  l = 0
  for r in range(len(array)):
    track[array[r]] += 1
    while len(track) > k:
      res = max(res, r-l)
      track[array[l]] -= 1
      if track[array[l]] == 0:
        del track[array[l]]
      l += 1
  
  return res


ans = findMaxSubarray([4,2,1,7,8,1,2,8,1,0], 3)
another = smallestSubarray([4,2,2,7,8,1,2,8,10], 8)
final = longestwithKdistinct(['A', 'A', 'H', 'H', 'H', 'H', 'C'], 2)
print("PASSED ONE" if ans == 16 else "FAILED ONE")
print("PASSED TWO" if another == 1 else "FAILED TWO")
print("PASSED THREE" if final == 6 else "FAILED THREE")


