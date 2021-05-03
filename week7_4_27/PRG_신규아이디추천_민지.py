def solution(new_id):
    # 1단계: 대문자 --> 소문자, 문자별로 나눠서 리스트에 넣기
    id_list = []
    id_list.extend(new_id.lower())
    # 2단계: 유효하지 않은 문자 제거
    valid_symbols = ['.', '-', '_']
    idx = 0
    while idx < len(id_list):
        if id_list[idx].isalnum() or id_list[idx] in valid_symbols:
            idx += 1
            continue
        id_list.pop(idx)
    # 3단계: 2번이상 연속된 마침표를 하나로 치환하면서 다시 스트링으로 변환
    answer = ''
    prev = '-'
    for i in id_list:
        if i == '.' and prev == '.':
            continue
        answer += i
        prev = i
    # 4단계: 앞뒤로 마침표 제거하기
    answer = answer.strip('.')
    # 5단계: new_id가 빈 문자열이라면, new_id에 'a' 대입
    if not answer:
        answer = 'a'
    # 6단계: 아이디의 길이가 16자 이상이라면 처음 15자만 채택
    if len(answer) >= 16:
        answer = answer[0:15].strip('.')
    elif len(answer) == 1:
        answer *= 3
    elif len(answer) == 2:
        answer += answer[1]
    return answer