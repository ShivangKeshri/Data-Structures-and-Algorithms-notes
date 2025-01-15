def maxval(arr):
  maxval = arr[0]
  maxval_index = 0
  for i in range(len(arr)):
    if arr[i] > maxval:
      maxval = arr[i]
      maxval_index = i
  return maxval_index
      
