def change(status):
    return "0" if status == "1" else "1"

def male(num):
    for i in range(1, N+1):
        if i >= num and i % num == 0:
            switches[i] = change(switches[i])

def female(num):
    i = 1
    while num - i > 0 and num + i < (N + 1) and switches[num-i] == switches[num+i]:
        switches[num-i] = change(switches[num-i])
        switches[num+i] = change(switches[num+i])
        i += 1
    switches[num] = change(switches[num])

N, switches = int(input()), ["0"] + input().split()

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        male(b)
    else:
        female(b)

for i in range(1, N+1):
    if i % 20 == 0:
        print(switches[i], end="\n")
    else:
        print(switches[i], end=" ")