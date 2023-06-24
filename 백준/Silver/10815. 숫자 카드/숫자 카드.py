N = int(input())
check = set(map(int, input().split()))
M = int(input())
print(*[1 if num in check else 0 for num in map(int, input().split())])