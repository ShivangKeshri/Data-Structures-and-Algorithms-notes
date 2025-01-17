def selection_sort(arr):
  for i in range(0, len(arr)-1):
    cur_min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[cur_min_index]:
        cur_min_index = j 
    min_value = arr.pop(cur_min_index)
    arr.insert(i, min_value)

print(selectionsort(arr))
