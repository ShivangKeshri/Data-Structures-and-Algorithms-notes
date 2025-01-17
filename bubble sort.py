def bubble_sort(arr):
  for i in range(0, len(arr)-1):
    swapped = False
    for j in range(0, len(arr)-1-i):
      if arr[j+1] > arr[j]:
        arr[j+1], arr[i] = arr[j], arr[j+1]
      swapped = True
    if not swapped:
      break
  
