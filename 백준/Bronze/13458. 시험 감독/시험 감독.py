N = int(input())
test_room = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for room in test_room:
    pre_result = max(room - B, 0)
    answer += 1
    if pre_result == 0:
        continue
    answer += pre_result // C + (1 if pre_result % C else 0)
print(answer)