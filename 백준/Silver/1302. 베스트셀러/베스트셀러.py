import sys;input = sys.stdin.readline
from collections import Counter

n = int(input().rstrip())
arr = Counter([input().rstrip() for _ in range(n)])
print(sorted(arr.most_common(), key=lambda x: (-x[1],x[0]))[0][0])