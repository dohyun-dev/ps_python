digit_dict = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def solution(s):
    tmp = ""
    answer = ""
    for c in s:
        if c.isdigit():
            answer += c
        else:
            tmp += c 
            if tmp in digit_dict:
                answer += digit_dict[tmp]
                tmp = ''
    return int(answer)