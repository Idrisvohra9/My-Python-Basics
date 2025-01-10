# Create a function that takes 2 lists, sorts the first one in ascending, second one in descending, does their subtraction and return the resulting array sorted in descending order. Do the sorting using selection sort


def sort_subtract(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    # Sorting the first array in ascending order:
    for i in range(l1 - 1):
        min_index = i
        for j in range(i + 1, l1):
            if arr1[j] < arr1[min_index]:
                min_index = j
        arr1[i], arr1[min_index] = arr1[min_index], arr1[i]
    print("First array after ascending sort: ", arr1)

    # Sorting the second array in descending order
    for i in range(l2 - 1):
        max_index = i
        for j in range(i + 1, l2):
            if arr2[j] > arr2[max_index]:
                max_index = j
        arr2[i], arr2[max_index] = arr2[max_index], arr2[i]
    print("Second array after descending sort", arr2)

    subtract_arr = []
    for i in range(l2):
        subtract_arr.append(arr1[i] - arr2[i])
    print("Subtraction result:", subtract_arr)

    for i in range(len(subtract_arr)):
        max_index = i
        for j in range(i + 1, l2):
            if subtract_arr[j] > subtract_arr[max_index]:
                max_index = j
        subtract_arr[i], subtract_arr[max_index] = (
            subtract_arr[max_index],
            subtract_arr[i],
        )
    print("Result sorted in descending order: ", subtract_arr)


sort_subtract([12, 2, 5, 9], [9, 6, 3, 10])
