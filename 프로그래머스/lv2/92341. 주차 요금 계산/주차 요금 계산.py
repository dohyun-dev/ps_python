from collections import defaultdict
import math

def calc_time(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(fees, records):
    record_dict = defaultdict(int)
    time_dict = defaultdict(int)
    
    for record in records:
        time, num, t = record.split()
        
        if t == "IN":
            record_dict[num] = calc_time(time)
        else:
            time_dict[num] += calc_time(time) - record_dict[num]
            del record_dict[num]
    
    for k, v in record_dict.items():
        time_dict[k] += calc_time('23:59') - v
        
    for k in time_dict.keys():
        time_dict[k] = max(0, time_dict[k] - fees[0])
    
    return [v for k, v in sorted([(k, fees[1] + int(math.ceil(v / fees[2])) * fees[3]) for k, v in time_dict.items()])]