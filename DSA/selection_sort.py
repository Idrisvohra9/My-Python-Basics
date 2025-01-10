# O(n^2) Quadratic Time
arr = [64, 25, 12, 22, 11]

l = len(arr)
for i in range(l - 1):
    min_index = i
    for j in range(i + 1, l):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]


print(arr)
"""
# The Algorithm to sort an array in ascending order using selection sort:

assign l as the length of the array

loop through the l-1 length of an array (because we will be swapping the current element with the minimum element and we don't want to swap the last element with itself)
    set the current index as the minimum index
    inside this loop another loop will go through the length of i + 1 (As we are comparing the current element with the element with the minimum index) and stop this loop when it reaches the length of the array
        if the value of the current element is less than the value of the element with the minimum index
            set the current index as the minimum index
    swap the current element with the element with the minimum index
"""
