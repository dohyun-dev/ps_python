H, M = map(int, input().split())
M = H * 60 + M - 45
M = 24 * 60 + M if M < 0 else M
print(f"{M // 60} {M % 60}")