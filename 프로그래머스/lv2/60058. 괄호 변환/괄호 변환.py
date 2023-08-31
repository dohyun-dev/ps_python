def split(string):
    open_, close_ = 0, 0
    for i, c in enumerate(string):
        if c == "(":
            open_ += 1
        else:
            close_ += 1
        if open_ == close_:
            return string[:i+1], string[i+1:]
        
def check(u):
    stack = []
    for c in u:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return False if stack else True
    
def solution(p):
    if not p:
        return p
    u, v = split(p)
    if check(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + "".join(")" if c == "(" else "(" for c in u[1:-1])
    