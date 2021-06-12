# 2018 KAKAO BLIND RECRUITMENT 압축

def solution(msg):
    answer, adds = [], []
    i, j, length = 0, 1, len(msg)

    while i < length:
        next_word = msg[i:j+1]
        if next_word in adds:
            if j >= length:
                answer.append(adds.index(next_word)+27)
                break
            j += 1
            continue
        now_word = msg[i:j]
        index = ord(now_word)-64 if len(now_word) <= 1 else adds.index(now_word)+27
        answer.append(index)
        adds.append(next_word)
        i = j
        j += 1
        
    return answer
