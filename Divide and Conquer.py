def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,4]))

# returning a sum using recursion
def recursive_sum(arr,i):
    total = 0 # base case if arr length = 0?
    i = arr[0]
    for i in range(len(arr)):
        recursive_sum(i + 1)
print(sum([1,14,56]))
