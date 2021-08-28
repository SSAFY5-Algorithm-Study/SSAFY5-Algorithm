def solution(table, languages, preference):
    answer = ''
    result = []
    
    languages_dict = dict()
    for i in range(len(languages)):
        languages_dict[languages[i]] = preference[i]
    
    
    result_dict = dict()
    for i in range(len(table)):
        x = table[i].split()
        x.reverse()
        total = 0
        for j in range(len(x)-1):
            if x[j] in languages_dict:
                total += languages_dict[x[j]] * (x.index(x[j]) + 1)
        result_dict[x[-1]] = total
        
    
    k = max(result_dict.values())
    for i,j in result_dict.items():
        if j == k:
            result.append(i)
    answer = sorted(result)[0]
    return answer