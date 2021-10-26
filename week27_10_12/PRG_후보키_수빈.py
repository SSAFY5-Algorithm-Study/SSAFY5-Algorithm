from itertools import combinations as comb

def solution(relation):    
    r = len(relation)
    c = len(relation[0])
    
    # 전체 조합 구하기
    all = []
    for i in range(1, c+1):
        all.extend(comb(range(c), i))

    # 유일성 만족하는 경우 찾기
    unique = []
    for a in all:
        temp = []
        for row in relation:
            temp.append(tuple([row[i] for i in a]))
        if len(set(temp)) == r:
            unique.append(a)

    # 최소성 만족하지 않는 경우 제거
    cadidate = set(unique)
    length = len(cadidate)
    for i in range(length):
        for j in range(i+1, length):
            # 교집합과 길이가 같은 경우 최소성 만족하지 않는 것
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                cadidate.discard(unique[j])
    
    return len(cadidate)