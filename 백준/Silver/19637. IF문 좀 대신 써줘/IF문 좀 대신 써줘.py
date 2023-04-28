def binary_search(arr, target):
    left, right, answer = 0, N - 1, ""
    while left <= right:
        mid = (left + right) // 2
        if target <= arr[mid][1]:
            answer = arr[mid][0]
            right = mid - 1
        else:
            left = mid + 1
    return answer


N, M = map(int, input().split())
name_arr = sorted(list(map(lambda x: [x[0], int(x[1])], [input().split() for _ in range(N)])), key=lambda x: x[1])
values = [int(input()) for _ in range(M)]

for value in values:
    print(binary_search(name_arr, value))