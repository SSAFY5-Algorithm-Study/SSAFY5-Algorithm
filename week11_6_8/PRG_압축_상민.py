'''
아이디어
1. 현재 입력에 글자를 하나씩 더해가면서 사전에 없는 것을 찾는다.
2. 사전에 추가해주고, 다음 글자가 없을 때까지 반복

'''


def solution(msg):
    # dictonary 형식으로 사전 생성
    word_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    # 사전 마지막 인색 번호 27로 저장
    last_idx = 27
    answer = []
    # 기본 설정
    current_word = ''
    msg_length = len(msg)
    idx = 0
    while True:
        # 인덱스가 msg의 마지막 글자를 넘어가면 종료
        if idx == msg_length:
            # 출력값 저장
            answer.append(temp)
            break
        # 현재 입력값
        current_word += msg[idx]
        # 만약, 현재 입력값이 존재하면, temp에 색인 번호 임시 저장
        if current_word in word_dict:
            temp = word_dict[current_word]
            idx += 1
        # 현재 입력값이 존재하지 않으면, temp를 answer에 추가
        # 사전에 현재 입력값과, 색인 번호를 저장
        # 색인 번호 + 1
        else:
            answer.append(temp)
            word_dict[current_word] = last_idx
            last_idx += 1
            # 현재 입력 초기화
            current_word = ''

    return answer