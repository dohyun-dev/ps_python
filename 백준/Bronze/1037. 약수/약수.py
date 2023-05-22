import sys; input = lambda : sys.stdin.readline().rstrip()

n, arr = int(input()), list(map(int, input().split()))
print(min(arr) * max(arr))