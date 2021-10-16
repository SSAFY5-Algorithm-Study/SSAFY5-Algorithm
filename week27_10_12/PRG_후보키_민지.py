from itertools import combinations

def solution(relation):
    N = len(relation[0])
    M = len(relation)
    columns = list(range(N))
    candidate_keys = []
    
    for i in range(1, N+1):
        combi = list(map(set, combinations(columns, i)))
        for c in combi:
            flag = 0
            # 이미 나온 후보키를 포함하고 있는지 확인
            for key in candidate_keys:
                if key.issubset(c):
                    flag = 1
                    break
            if flag:
                continue
                
            # 새로운 후보키가 될 수 있는지 확인
            unique = set()
            for row in relation:
                temp = []
                for col in c:
                    temp.append(row[col])
                unique.add(tuple(temp))
            
            if len(unique) == M:
                candidate_keys.append(c)
        
    return len(candidate_keys)