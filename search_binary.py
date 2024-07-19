def binary_search(arr, target):
    #Your implementation here
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#Test the function
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7
result = binary_search(sorted_list, target_value)
print(result)
