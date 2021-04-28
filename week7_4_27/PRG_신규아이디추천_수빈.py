def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 리스트로 바꾸는 경우
    # 2단계
    # second = []
    # for c in new_id:
    #     if c.isalnum():
    #         second.append(c)
    #     elif c in ['-', '_', '.']:
    #         second.append(c)
    # 3단계
    # third = ''
    # for i in range(len(second) - 1):
    #     if second[i] == '.' and second[i+1] == '.':
    #         continue
    #     third += second[i]
    # if second[-1] != '.':
    #     third += second[-1]


    # 리스트로 안 바꾸고 싶다..!
    # 2단계
    for c in new_id:
        if c.isalnum() or c in ['-', '_', '.']:
            answer += c
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = third.strip('.')

    # 5단계
    if not answer:
        answer = 'a'
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer


# 정규 표현식으로도 가능..?!
