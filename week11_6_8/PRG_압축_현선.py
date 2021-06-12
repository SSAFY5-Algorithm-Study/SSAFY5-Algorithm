# 접근 : 걍 지문 내용 하나씩 따라가기.

def solution(msg):
    answer = []
    # 알파벳 : 숫자 로 이루어진 딕셔너리 생성
    alpha = [chr(i) for i in range(65,91)]
    alpha_dict = {j : i+1 for i,j in enumerate(alpha)}
    
    i = 0
    key_num = 27
    # 문자열의 범위를 바꿔줄 변수
    k = 1
    while i < len(msg) and k <= len(msg):
        # 슬라이싱으로 문자열 가져옴. 처음은 하나씩 가져옴
        w = msg[i:k]
        # 만약 그 문자가 딕셔너리에 있으면 k를 1 증가시켜서 문자 하나 더 추가할거야
        if w in alpha_dict.keys():
            k += 1
        # 아니면, 그 문자열 직전의 문자열의 value값 answer에 추가해주고,
        # 그 문자열을 딕셔너리에 추가해주기. 번호 키값으로 붙여서.
        else:
            w_past = msg[i:k-1]
            answer.append(alpha_dict.get(w_past))
            alpha_dict[w] = key_num
            i = k-1
            key_num += 1
    # 맨 마지막 남은거 추가.
    answer.append(alpha_dict.get(w))
    return answer