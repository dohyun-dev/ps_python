def calc_date(date):
    year, month, date = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + date

def solution(today, terms, privacies):
    today = calc_date(today)
    terms_dict = {t[0]: int(t[2:]) * 28 for t in terms}
    answer = []
    
    for i, privacy in enumerate(privacies, 1):
        date, kind = privacy.split()
        pivacy_date = calc_date(date) + terms_dict[kind]
        
        if today >= pivacy_date:
            answer.append(i)
    return answer