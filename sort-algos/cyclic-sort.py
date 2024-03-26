'''
  @ used for arrays holding 1 to N values
  @ if N in array just skip over
  @ N = len of unsorted array
  @ O(n) runtime
'''

def cyclic_sort(array):
  i = 0
  while i < len(array):
    val = array[i]
    if val-1 != i:
      array[i], array[val-1] = array[val-1], array[i]
    else:
      i += 1
  return array

arr = [3, 2, 1]
print(arr)
print(cyclic_sort(arr))
