def solution(table, languages, preference):
    ind_score_dict = {}
    max_score = 0
    max_ind = ""
    
    # STEP 1: table data 가공하기
    # {SI: {JAVA: 5, JAVASCRIPT: 4, SQL: 3, PYTHON: 2, C#: 1}, CONTENTS:...}
    for data in table:
        # STEP 1.1
        # 완료 시 결과물: ["SI", "JAVA", "JAVASCRIPT", "SQL", "PYTHON", "C#"]
        row = data.split(" ")
        # STEP 1.2
        # 완료 시 결과물: key = "SI"
        key = row.pop(0)
        scores = {}
        score = 5
        # STEP 1.3
        # 완료 시 결과물: {"JAVA": 5, "JAVASCRIPT": 4, "SQL": 3, "PYTHON": 2, "C#": 1}
        for language in row:
            scores[language] = score
            score -= 1
        # STEP 1.4
        # 완료 시 결과물: {"SI": {"JAVA": 5, "JAVASCRIPT": 4, "SQL": 3, "PYTHON": 2, "C#": 1}}
        ind_score_dict[key] = scores
    
    # STEP 2: 각 직업군 별로 점수 계산
    for ind in ind_score_dict.keys():
        total = 0
        # 2.1 각 직업군 별로 점수 조회
        for i in range(len(languages)):
            lang = languages[i]
            pref = preference[i]
            total += ind_score_dict[ind].get(lang, 0) * pref
        
        # 2.2 최대 점수 직업군 찾기
        # 점수가 동률이라면 사전순으로 낮은 값 찾기
        if total == max_score:
            max_ind = min(max_ind, ind)
        elif total > max_score:
            max_ind = ind
        max_score = max(total, max_score)
        
    return max_ind