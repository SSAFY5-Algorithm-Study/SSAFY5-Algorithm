# 효율성 0점
def solution(info, query):
    answer = []
    for i in range(len(info)):
        info[i] = info[i].split()
    
    for q in query:
        base = q.split()
        condition = list(set(base[:7]))
        condition.remove('and')
        if '-' in condition:
            condition.remove('-')
        condition = set(condition)
        candidate = 0
        for i in info:
            if int(i[-1]) >= int(base[-1]):
                i = set(i)
                if i.intersection(condition) == condition:
                    candidate += 1
        answer.append(candidate)
    return answer