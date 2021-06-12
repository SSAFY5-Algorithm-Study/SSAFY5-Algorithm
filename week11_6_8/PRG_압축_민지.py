import string

def solution(msg):
    answer = []
    # 검사하는 문자열의 start와 end 지점
    start = end = 0
    # dictionary에 추가할 value값
    dict_idx = 27
    # A ~ Z까지 저장해놓은 dictionary
    LZW_dict = dict(zip(string.ascii_uppercase, range(1, 27)))
    

    while start < len(msg) and end <= len(msg):
        # 현재 검사하는 문자열을 LZW_dict에서 찾고, 있으면 idx값을, 없으면 False를 temp에 저장한다
        substr = msg[start:end+1]
        temp = LZW_dict.get(substr, False)
        # 만약 해당 문자열을 찾았다면
        if temp:
            idx = temp # 찾은 인덱스
            end += 1 # 글자 길이를 하나 늘려서 검사
        # 못찾았다면
        else:
            # 가장 최근에 찾은 단어의 인덱스를 추가
            answer.append(idx)
            # 못찾은 지점부터 다시 인덱스를 새로 시작
            start = end
            # 못찾은 단어를 LZW_dict에 추가
            LZW_dict[substr] = dict_idx
            dict_idx += 1
    # 마지막 찾은 단어는 anwer 배열에 추가가 안되있기 때문에 추가
    answer.append(idx)
    return answer

print(solution('ABABABA'))