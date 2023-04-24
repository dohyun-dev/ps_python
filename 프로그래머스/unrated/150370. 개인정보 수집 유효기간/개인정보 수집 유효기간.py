# 날짜를 받아서 day로 변환
# 각 정책에 따라 day +
# 현재 날짜와 비교해 더 크다면 폐기

def calc_day(date):
    date = list(map(int, date.split(".")))
    return date[0] * 12 * 28 + date[1] * 28 + date[2]

def solution(today, terms, privacies):
    today = calc_day(today)
    terms_dict = {t[0]: int(t[2:]) * 28 for t in terms}
    answer = []
    
    for idx, v in enumerate(privacies, 1):
        date, terms_name = v.split()
        date = calc_day(date)
        if today >= date + terms_dict[terms_name]:
            answer.append(idx)
    return answer