# 날짜를 받아서 day로 변환
# 각 정책에 따라 day +
# 현재 날짜와 비교해 더 크다면 폐기

def calc_day(year, month, day):
    return year * 12 * 28 + (month - 1) * 28 + day

def solution(today, terms, privacies):
    today = list(map(int, today.split(".")))
    today = calc_day(today[0], today[1], today[2])
    terms_dict = {}
    answer = []
    
    for term in terms:
        name, period = term.split()
        terms_dict[name] = int(period) * 28
    
    for idx, v in enumerate(privacies, 1):
        date, terms_name = v.split()
        date = list(map(int, date.split(".")))
        if today >= calc_day(date[0], date[1], date[2]) + terms_dict[terms_name]:
            answer.append(idx)
    return answer