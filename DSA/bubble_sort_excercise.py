# A function that takes 2 list and sorts the first one in ascending order and the second one in descending order, does their sum and sorts the sum in ascending order and returns the result


def sort_sum(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    # Sorting the first list in ascending order
    for i in range(l1 - 1):
        for j in range(l1 - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
    print("Sorted first list:", arr1)
    # Sorting the second list in descending order
    for i in range(l2 - 1):
        for j in range(l2 - i - 1):
            if arr2[j] < arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    print("Sorted second list:", arr2)
    sumArr = []
    # Summing the two lists
    for i in range(l1):
        sumArr.append(arr1[i] + arr2[i])
    print("Sum of elements", sumArr)
    # Sorting the sum list in ascending order
    for i in range(len(sumArr) - 1):
        for j in range(len(sumArr) - i - 1):
            if sumArr[j] > sumArr[j + 1]:
                sumArr[j], sumArr[j + 1] = sumArr[j + 1], sumArr[j]
    return sumArr

arr1 = [10, 8, 50, 40, 20]
arr2 = [5, 10, 20, 15, 95]
print(sort_sum(arr1, arr2))