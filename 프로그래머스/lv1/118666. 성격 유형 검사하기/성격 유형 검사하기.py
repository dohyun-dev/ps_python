def solution(survey, choices):
    counter = {c: 0 for c in ('R', 'T', 'C', 'F', 'J', 'M', 'A', 'N')}
    for s, c in zip(survey, choices):
        if c < 4:
            counter[s[0]] += 4 - c
        else:
            counter[s[1]] += c - 4            
    answer = 'R' if counter['R'] >= counter['T'] else 'T'
    answer += 'C' if counter['C'] >= counter['F'] else 'F'
    answer += 'J' if counter['J'] >= counter['M'] else 'M'
    answer += 'A' if counter['A'] >= counter['N'] else 'N'
    return answer