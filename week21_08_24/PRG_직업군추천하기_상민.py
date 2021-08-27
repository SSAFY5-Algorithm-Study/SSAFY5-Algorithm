# 언어 선호도(preference) X 직업군 언어 점수(table)
# 반환: 총합이 가장 높은 직업군 (Job) -> 같을 경우, 사전 순(sort)

def solution(table, languages, preference):
    score_board = [0 ,5, 4, 3, 2, 1]
    job_board = ['SI', 'CONTENTS', 'HARDWARE', 'PORTAL', 'GAME']
    table_dict = {}
    # 점수 딕셔너리 생성
    for detail in table:
        splitted_info = detail.split()
        for i in range(len(splitted_info)):
            if i == 0:
                table_key = splitted_info[i]
                table_dict[splitted_info[i]] = {}
            else:
                table_dict[table_key][splitted_info[i]] = score_board[i]
    answer = []
    max_score = -987654321
    for job in job_board:
        job_score = 0
        for user_info in list(zip(languages, preference)):
            lang, pref = user_info
            existed_score = table_dict[job].get(lang)
            if existed_score:
                job_score += existed_score * pref
        if job_score > max_score:
            if answer:
                answer.pop()
            answer.append(job)
            max_score = job_score
        elif job_score == max_score:
            answer.append(job)
    
    return sorted(answer)[0]
