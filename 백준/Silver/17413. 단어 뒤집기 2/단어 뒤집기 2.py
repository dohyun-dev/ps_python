stack, flag = [], False
answer = ""
for c in input():
    if flag:
        if c == ">":
            flag = False
        answer += c
    else:
        if c == " " or c == "<":
            while stack:
                answer += stack.pop()
            if c == "<":
                flag = True
            answer += c
        else:
            stack.append(c)
while stack:
    answer += stack.pop()
print(answer)