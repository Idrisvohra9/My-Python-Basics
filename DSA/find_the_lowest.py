# O(n) Constant Time
arr = [10, 12, 5, 8, 9, 13]
lowest = arr[0]
for i in range(len(arr)):
    if arr[i] > lowest:
        lowest = arr[i]

print("The lowest value is", lowest)

"""
# The Algorithm to Find the lowest value in an array:

assume/assign the lowest value to be the value at the first index
loop through the entire length of the array
    if the value at the current index is lower then the assumed value at the first index 
        re-assign that lower variable value to the current value at the index

"""
