def TwoSum(arr):
    target = arr[0]
    pairs = []
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append(f"{arr[i]},{arr[j]}")
    return " ".join(pairs)


arr = [7, 3, 5, 2, -4, 8, 11]
print(TwoSum(arr))
