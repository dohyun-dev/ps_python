import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^a-z0-9-_.]+", "", answer)
    answer = re.sub("\.+", ".", answer)
    answer = re.sub("^\.|\.$", "", answer).strip()
    answer = answer if answer else "a"
    answer = answer[:15]
    answer = answer[:-1] if answer[-1] == '.' else answer
    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    return answer