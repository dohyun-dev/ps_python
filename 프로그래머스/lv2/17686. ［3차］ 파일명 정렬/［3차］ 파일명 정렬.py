import re

def solution(files):
    tmp = []
    for idx, file in enumerate(files):
        m = re.match('([a-zA-Z\s.-]+)([\d]{1,5})([a-zA-Z0-9\s.-]*)', file)
        tmp.append((idx, m.group(1), m.group(2), m.group(3)))
    tmp.sort(key=lambda x: (x[1].lower(), int(x[2]), idx))
    return ["".join(x[1:]) for x in tmp]