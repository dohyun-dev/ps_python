from collections import defaultdict

counter = defaultdict(int)
for _ in range(int(input())):
    file_name, file_type = input().split(".")
    counter[file_type] += 1
print("\n".join(map(lambda x: f"{x} {counter[x]}", sorted(counter.keys()))))