def solution(table, languages, preference):
    ind_score_dict = {}
    max_score = 0
    max_ind = ""
    
    # table data 가공하기
    # {SI: {JAVA: 5, JAVASCRIPT: 4, SQL: 3, PYTHON: 2, C#: 1}, CONTENTS:...}
    for data in table:
        row = data.split(" ")
        key = row.pop(0)
        scores = {}
        score = 5
        for language in row:
            scores[language] = score
            score -= 1
        ind_score_dict[key] = scores
    
    # 각 분야별로 점수 계산
    for ind in ind_score_dict.keys():
        total = 0
        # 각 언어 별로
        for i in range(len(languages)):
            lang = languages[i]
            pref = preference[i]
            total += ind_score_dict[ind].get(lang, 0) * pref
        
        if total == max_score:
            max_ind = min(max_ind, ind)
        elif total > max_score:
            max_ind = ind
        max_score = max(total, max_score)
        
    return max_ind