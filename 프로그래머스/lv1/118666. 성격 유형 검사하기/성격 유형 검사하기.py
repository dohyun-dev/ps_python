def solution(survey, choices):
    personal_dict = {c: 0 for c in "RTCFJMAN"}
    check = {c: False for c in "RTCFJMAN"}
    answer = ""
    
    for s, c in zip(survey, choices):
        if c < 4:
            personal_dict[s[0]] += 4 - c
        elif c > 4:
            personal_dict[s[1]] += c - 4
            
    for word in ["RT", "CF", "JM", "AN"]:
        if personal_dict[word[0]] >= personal_dict[word[1]]:
            answer += word[0]
        else:
            answer += word[1]
            
    return answer