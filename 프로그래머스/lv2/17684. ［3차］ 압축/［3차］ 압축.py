def solution(msg):
    word_dict = {chr(ord('A') + i): i + 1 for i in range(26)}
    answer = []
    w = ""
    
    for c in msg:
        w += c
        if w not in word_dict:
            answer.append(word_dict[w[:-1]])
            word_dict[w] = len(word_dict) + 1
            w = c

    answer.append(word_dict[w])
    return answer