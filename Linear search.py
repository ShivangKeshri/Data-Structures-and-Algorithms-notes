# the linear search below returns the index.

def linearsearch(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1


