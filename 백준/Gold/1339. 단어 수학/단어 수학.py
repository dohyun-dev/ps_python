from collections import Counter

def calc(word, counter):
    total = 0
    total += counter[word] - 1
    return total

N = int(input())
arr = [input() for _ in range(N)]
word_counter = Counter()
check_num, convert_dict = 9, {}
max_length = max(len(c) for c in arr)
answer = []

for word in arr:
    word = "0" * (max_length - len(word)) + word
    for i in range(max_length):
        if word[i] == "0":
            continue
        word_counter[word[i]] += 10 ** (5 - i)

offset = 9
for key, value in word_counter.most_common():
    convert_dict[key] = str(offset)
    offset -= 1

print(sum(int("".join([convert_dict[c] for c in word])) for word in arr))