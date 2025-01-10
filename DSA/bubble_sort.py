# O(n^2) Quadratic Time
arr = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(arr)
for i in range(n - 1):
    # This inner loop compares adjacent elements and swaps them if needed
    # It runs from index 0 to n-i-1 because after each outer loop iteration,
    # the last i elements are already sorted
    swapped = False  # Set sorted to false for checking if the array is swapped once or not, if it stays false it means that the array doesn't need to get swapped and it is already sorted
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # If it is swapped
            swapped = True
    if not swapped:
        break

print("Sorted array is:", arr)
"""
# The Algorithm to sort in ascending order using bubble sort:

loop through the n-1 length of an array (because we will be swapping/bubbling the biggest value to the last index)
    inside this loop another loop will go through the length of n - the index of the upper loop(because after each outer loop iteration, the last i elements are already sorted) - 1
        if the current element is greater than the next element, swap them
"""
