import sys
input = sys.stdin.readline

def binary_search(arr, target):
    left, right = 0, N - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return "1"
    return "0"

N, arr = int(input()), sorted(list(map(int, input().split())))
M, targets = int(input()), list(map(int, input().split()))

for target in targets:
    print(binary_search(arr, target), end=" ")