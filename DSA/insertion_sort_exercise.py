# Write a program to sort an array of n integers using the insertion sort algorithm.

# The program should:

# Accept an unsorted array of integers as input.
# Sort the array in ascending order using insertion sort.
# Output the sorted array.

def sort_asc(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_value = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] < current_value:
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr

print(sort_asc([10, 20, 6, 12, 30]))