def binary_search(arr, target1, target2):
    left, right = 0, N - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target1:
            right = mid - 1
        else:
            left = mid + 1

    answer1 = left

    left, right = 0, N - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target2:
            left = mid + 1
        else:
            right = mid - 1
    answer2 = right

    return answer2 - answer1 + 1

N, M = map(int, input().split())
points = sorted(list(map(int, input().split())))
answer = []
for _ in range(M):
    left, right = map(int, input().split())
    answer.append(binary_search(points, left, right))
print(*answer, sep="\n")