from collections import deque, defaultdict

def search(folder):
    q = deque([folder])
    answer = []

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for next in file_dict[cur][1]:
                if file_dict[next][0] == "1":
                    q.append(next)
                else:
                    answer.append(next)
    return f"{len(set(answer))} {len(answer)}"

N, M = map(int, input().split())
file_dict = defaultdict()
input_data = [input().split() for _ in range(N+M)]
answer = []

for a, b, c in input_data:
    file_dict[a] = ["1", set()]
    if c == "1":
        file_dict[b] = ["1", set()]
    else:
        file_dict[b] = ["0"]

for a, b, c in input_data:
    file_dict[a][1].add(b)

for _ in range(int(input())):
    answer.append(search(input().split("/")[-1]))

print("\n".join(answer))