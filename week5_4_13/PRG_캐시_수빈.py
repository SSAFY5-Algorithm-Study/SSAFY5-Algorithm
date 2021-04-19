# def solution(cacheSize, cities):
#     # 소문자로 변환
#     for i in range(len(cities)):
#         cities[i] = cities[i].lower()
#     # 캐시 크기가 0이면 모두 cache miss
#     if not cacheSize:
#         answer = 5 * len(cities)
#     else:
#         cache = []
#         answer = 0
#         for city in cities:
#             if len(cache) < cacheSize:
#                 # cache hit
#                 if city in cache:
#                     answer += 1
#                     pos = cache.index(city)
#                     cache.append(cache.pop(pos))
#                 # cache miss
#                 else:
#                     answer += 5
#                     cache.append(city)
#             else:
#                 # cache hit
#                 if city in cache:
#                     answer += 1
#                     pos = cache.index(city)
#                     cache.append(cache.pop(pos))
#                 # cache miss
#                 else:
#                     answer += 5
#                     cache.pop(0)
#                     cache.append(city)
#     return answer


# 좀 더 간단하게...? 
# 더 효율적인 방법이 존재할 것만 같다..
def solution(cacheSize, cities):
    # 소문자로 변환
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    # 캐시 크기가 0이면 모두 cache miss
    if not cacheSize:
        answer = 5 * len(cities)
    else:
        cache = []
        answer = 0
        for city in cities:
            # cache hit
            if city in cache:
                answer += 1
                # pos = cache.index(city)
                # cache.append(cache.pop(pos))
                cache.remove(city)
                cache.append(city)
            # cache miss
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                answer += 5
                cache.append(city)
    return answer