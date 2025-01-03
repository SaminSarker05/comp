"""
NOTES:
- LOG(N) time complexity
- finding element in sorted array
"""

def binarysearch(array, target):
  array.sort()
  l, r = 0, len(array) - 1
  while l <= r:
    mid = (l + r) // 2
    if array[mid] == target: return mid
    if target < array[mid]:
      r = mid - 1
    elif target > array[mid]:
      l = mid + 1
  
  return -1

print(binarysearch([1,2,3,4], 1))
