def solution(cacheSize, cities):
    temp = ['empty'] * cacheSize
    cities = temp + cities
    start = 0
    answer = 0
    for i in range(cacheSize, len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in cities[start:i]:
            answer += 1
        else:
            answer += 5
        start += 1
    return answer