N, M = map(int, input().split())
lights = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        lights[b-1] = c
    elif a == 2:
        lights = lights[:b-1] + list(map(lambda x: 0 if x else 1, lights[b-1: c])) + lights[c:]
    elif a == 3:
        lights = lights[:b-1] + [0] * (c - b + 1) + lights[c:]
    else:
        lights = lights[:b-1] + [1] * (c - b + 1) + lights[c:]
print(" ".join(map(lambda x: str(x), lights)))