
# Finding the Minimum Value in an array

def find_min(arr):
    min_val = arr[0]
    min_val_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_val_index = i
    return min_val, min_val_index

arr = [64, 34, 25, 5, 22, 11, 90, 12]
print(find_min(arr)) # --> output : (5,3)


# another way to find only the MINIMUM VALUE(element):

def find_minn(arr):
    smallest = arr[0]
    
    for i in arr:
        if i < smallest:
            smallest = i

    return smallest

arr = [64, 34, 25, 5, 22, 11, 90, 12]
print(find_minn(arr)) # --> output : 5 because the index i looks at the elements only in this case
