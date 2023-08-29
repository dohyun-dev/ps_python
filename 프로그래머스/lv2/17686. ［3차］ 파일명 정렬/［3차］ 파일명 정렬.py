import re

def solution(files):
    tmp = []
    for idx, file in enumerate(files):
        tmp.append((idx, *re.match('([a-zA-Z-. ]+)(\d{1,5})(.*)', file).groups()))
    tmp.sort(key=lambda x: (x[1].lower(), int(x[2]), idx))
    return ["".join(x[1:]) for x in tmp]