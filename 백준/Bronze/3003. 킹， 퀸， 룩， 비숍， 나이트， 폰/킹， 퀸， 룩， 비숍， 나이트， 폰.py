data = list(map(int, input().split()))
arr = [1, 1, 2, 2, 2, 8]
for i in range(len(data)):
    print(arr[i] - data[i], end=" ")