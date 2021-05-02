def solution(new_id):
    answer = ''
    # 단계별로 처리하기.
    # 1단계 ~ 2단계 한번에 처리가능할듯?
    no_alpah_num = {'-','_','.'}
    for i in range(len(new_id)):
        if 65 <=ord(new_id[i]) <= 90:
            answer += new_id[i].lower()
        elif 48 <=ord(answer[i]) <= 57 or (answer[i] in no_alpah_num):
            answer += new_id[i]
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..','.')
    
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if answer == '':
        answer += 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer