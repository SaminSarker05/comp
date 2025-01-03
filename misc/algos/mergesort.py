"""
NOTES:
- NLOG(N) time complexity
- break array into smaller parts
- merge two halvs in recursive manner
"""

def mergesort(array):
  if len(array) == 1: return array
  mid = len(array) // 2
  l = mergesort(array[: mid])
  r = mergesort(array[mid: ])
  return merge(l, r)


def merge(left, right):
  p1, p2 = 0, 0
  res = []
  while p1 < len(left) and p2 < len(left):
    if left[p1] <= right[p2]: 
      res.append(left[p1])
      p1 += 1
    else:
      res.append(right[p2])
      p2 += 1
  
  while p1 < len(left):
    res.append(left[p1])
    p1 += 1
  
  while p2 < len(right):
    res.append(right[p2])
    p2 += 1
  return res

