sound = list(input())
check = [0] * len(sound)
word_dict = {"q": "u", "u": "a", "a": "c", "c": "k", "k": "q"}
answer = 0

for i in range(len(sound)):
    if check[i] or sound[i] != "q":
        continue
    pre_word = "q"
    check[i] = True
    for j in range(i+1, len(sound)):
        if check[j]:
            continue
        if word_dict[pre_word] == sound[j]:
            check[j] = 1
            pre_word = word_dict[pre_word]
    if pre_word == "k":
        answer += 1
    else:
        answer = -1
        break
print(answer if all(check) else -1)