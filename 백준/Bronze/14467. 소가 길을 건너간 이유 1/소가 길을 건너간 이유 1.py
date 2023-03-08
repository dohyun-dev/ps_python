N = int(input())
answer, status_dict = 0, {}

for _ in range(N):
    a, b = map(int, input().split())
    if a not in status_dict:
        status_dict[a] = b
    else:
        if status_dict[a] != b:
            status_dict[a] = b
            answer += 1
print(answer)