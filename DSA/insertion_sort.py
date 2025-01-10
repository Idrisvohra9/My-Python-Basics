my_array = [64, 34, 25, 12, 22, 11, 90, 5]  # Initialize an unsorted array

# Get the length of the array
n = len(my_array)

# Start from the second element (index 1) and iterate through the array (as we assume the first element is already sorted on its own)
for i in range(1, n):
    # Keep track of where we will insert the current element
    insert_index = i
    # Store the current element we are trying to insert
    current_value = my_array[i]
    # print(my_array)
    # Look at each element before the current element, moving right to left
    for j in range(i - 1, -1, -1):
        # If the element we're looking at is bigger than our current value
        if my_array[j] > current_value:
            # Shift that element one position to the right
            my_array[j + 1] = my_array[j]
            # Update where we will insert our current value
            insert_index = j
        else:
            # If we find a smaller element, we've found the right spot to insert
            break

    # Insert the current value at its correct position
    my_array[insert_index] = current_value

print("Sorted array:", my_array)

"""
Algorithm for Insertion Sort:
1. Start with the first element as a sorted portion
2. Take the next element and store it as current_value
3. Compare current_value with each element in the sorted portion from right to left
4. If an element is greater than current_value, shift it one position to the right
5. When a smaller element is found or beginning is reached, insert current_value at that position
6. Repeat steps 2-5 until all elements are sorted
7. The array is now sorted in ascending order
"""
