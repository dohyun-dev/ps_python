N, M = map(int, input().split())
trains = [[False] * 20 for _ in range(N)]
check = set()
answer = 0

for _ in range(M):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        trains[oper[1]-1][oper[2]-1] = True
    elif oper[0] == 2:
        trains[oper[1]-1][oper[2]-1] = False
    elif oper[0] == 3:
        for i in range(19, 0, -1):
            trains[oper[1]-1][i] = trains[oper[1]-1][i-1]
        trains[oper[1]-1][0] = False
    else:
        for i in range(19):
            trains[oper[1]-1][i] = trains[oper[1]-1][i+1]
        trains[oper[1]-1][19] = False

for train in trains:
    tmp = "".join(map(lambda x: "1" if x else "0", train))
    if tmp not in check:
        answer += 1
    check.add(tmp)
print(answer)