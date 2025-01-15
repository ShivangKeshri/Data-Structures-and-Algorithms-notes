def binarysearch(arr, target):
  low = 0
  high = len(arr) -1
  while low <= high :
    mid = (high + low)//2
    guess = arr[mid]

    if guess == target:
      return mid
    elif guess > target:
      high = mid -1
    else:
      low = mid + 1
  return -1 # returns -1 if low !<= high

# binary search only works on sorted arrays.
