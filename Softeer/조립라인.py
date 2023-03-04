N = int(input())
A, B = [0] * N, [0] * N
a_move, b_move = [0] * N, [0] * N
for i in range(N-1):
    A[i], B[i], a_move[i], b_move[i] = map(int, input().split())
A[N-1], B[N-1] = map(int, input().split())

dp_A = [0] * (N+1)
dp_B = [0] * (N+1)
dp_A[0], dp_B[0] = A[0], B[0]

for i in range(1, N):
    dp_A[i] = min(dp_A[i-1], dp_B[i-1] + b_move[i-1]) + A[i]
    dp_B[i] = min(dp_B[i-1], dp_A[i-1] + a_move[i-1]) + B[i]
print(min(dp_A[N-1], dp_B[N-1]))