def selectionsort(arr):
  for i in range(0,len(arr)-1):
    cur_min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[cur_min_index]
        cur_min_index = j
    arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]


print(selectionsort(arr))
    
