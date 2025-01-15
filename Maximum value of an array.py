# finding the Maximum value in an array
# i represents the value of each element.


def max_val(array):
    maxval = array[0]]
    maxval_index = 0
    for i in range(1,len(array)):  # this is fine for looping over the elements in the array.
        if array[i] > maxval: # If the element is greater than the initalized maxval, we find get the element.
            maxval = array[i]
            maxval_index = i
    return maxval, maxval_index

array = [1,2,6,8,9,-1]
print("the largest value is value, index : ", max_val(array))
      
