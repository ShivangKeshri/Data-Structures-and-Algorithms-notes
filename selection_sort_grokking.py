def minimum_value(arr):
  min_val = arr[0]
  min_val_index = 0

  for i in range(1, len(arr)):
    if arr[i] < min_val:
      min-val = arr[i]
      min_val_index = i
  return min_val_index

def selectionsort(arr):
  newArr = []
  for i in range(len(arr)):
   smallest = findSmallest(arr)
   newArr.append(arr.pop(smallest))
  return newArr
