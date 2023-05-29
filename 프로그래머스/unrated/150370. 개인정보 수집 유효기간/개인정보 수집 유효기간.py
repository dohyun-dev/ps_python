def convert_stamp(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    terms_dict = {term[0]: int(term[2:]) * 28 for term in terms}
    today = convert_stamp(today)
    answer = []
    for idx, privacy in enumerate(privacies, 1):
        if today >= convert_stamp(privacy[:-2]) + terms_dict[privacy[-1]]:
            answer.append(idx)
    return answer