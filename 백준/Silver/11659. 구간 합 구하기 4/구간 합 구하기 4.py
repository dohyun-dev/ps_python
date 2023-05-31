N, M = map(int, input().split())
arr = [0]

for num in map(int, input().split()):
    arr.append(num + arr[-1])

for _ in range(M):
    a, b = map(int, input().split())
    print(arr[b] - arr[a-1])