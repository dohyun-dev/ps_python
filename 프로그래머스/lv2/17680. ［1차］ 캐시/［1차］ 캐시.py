def solution(cacheSize, cities):
    
    def LRU(city):
        flag = False
        if city in cache:
            flag = True
            cache.remove(city)
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
        cache.append(city)
        return flag
        
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            answer += 5
            continue
            
        if LRU(city):
            answer += 1
        else:
            answer += 5
    return answer