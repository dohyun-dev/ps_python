def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return 1
    return 0

N = int(input())
nums = sorted(list(map(int, input().split())))
M = int(input())

for num in map(int, input().split()):
    print(binary_search(nums, num))