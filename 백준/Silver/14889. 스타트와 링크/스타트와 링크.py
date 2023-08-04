def calc_stat(team):
    total = 0
    for i in range(len(team)):
        player1 = team[i]
        for j in range(i + 1, len(team)):
            player2 = team[j]
            total += players[player1][player2] + players[player2][player1]
    return total

def make_team(l, team1=[], team2=[]):
    global answer
    if len(team1) > N // 2 or len(team2) > N // 2:
        return
    if l == N:
        gap = abs(calc_stat(team1) - calc_stat(team2))
        answer = min(answer, gap)
        return
    make_team(l + 1, team1 + [l], team2)
    make_team(l + 1, team1, team2 + [l])


N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")
make_team(0)
print(answer)