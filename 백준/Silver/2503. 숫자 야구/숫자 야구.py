def calc(answer):
    for a, s, b in arr:
        strike, ball = 0, 0
        for i in range(3):
            if a[i] == answer[i]:
                strike += 1
            elif a[i] in answer:
                ball += 1
        if int(s) != strike or int(b) != ball:
            break
    else:
        return True

    return False

def permu(l=0, result=""):
    if l == 3:
        if calc(result):
           answer.append(result)
        return

    for i in range(1, 10):
        if check[i]:
            continue
        check[i] = True
        permu(l+1, result+str(i))
        check[i] = False

N = int(input())
arr, check = [input().split() for _ in range(N)], [False] * 11
answer = []
permu()
print(len(answer))