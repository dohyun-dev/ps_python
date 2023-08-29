import re
from collections import Counter

# 1. 공백 및 소문자 변환
# 2. 두글자씩 쪼개기
# 3. 글자 쌍이 영문자인지 확인
# 4, 유사도 구하기 counter

def solution(str1, str2):
    counter1 = Counter(filter(lambda x: re.search('[a-z]{2}', x), [str1[i:i+2].lower() for i in range(len(str1) - 1)]))
    counter2 = Counter(filter(lambda x: re.search('[a-z]{2}', x), [str2[i:i+2].lower() for i in range(len(str2) - 1)]))
    result1 = sum((counter1 & counter2).values())
    result2 = sum((counter1 | counter2).values())
    return 65536 if result2 == 0 else int(result1 / result2 * 65536)

    
    
    