def solution(record):
    nickname_dict = {}
    answer = []
    
    for r in record:
        r = r.split()
        
        if r[0] in ["Enter", "Change"]:
            nickname_dict[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            answer.append(f"{nickname_dict[r[1]]}님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(f"{nickname_dict[r[1]]}님이 나갔습니다.")
    
    return answer