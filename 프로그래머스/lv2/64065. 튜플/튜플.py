import re
from collections import Counter

def solution(s):
    
    return [int(k) for k, v in sorted(Counter(re.findall('[0-9]+', s)).most_common(), key=lambda x: -x[1])]