import sys; sys.setrecursionlimit(10**5)

def check(word, cnt=0):
    global flag
    left, right = 0, len(word) - 1
    while left <= right:
        if word[left] == word[right]:
            left, right = left + 1, right - 1
        elif cnt == 0:
            check(word[left+1:right+1], cnt + 1)
            if flag == 2:
                check(word[left:right], cnt + 1)
            break
        else:
            break
    if right < left:
        flag = cnt

answer = []
for _ in range(int(input())):
    flag = 2
    check(input())
    answer.append(f'{flag}')
print(*answer, sep="\n")