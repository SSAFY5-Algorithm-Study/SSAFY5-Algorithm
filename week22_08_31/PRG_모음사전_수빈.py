def solution(word):
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    # 지리수별 순서값
    # 1
    # AAAAA : 5
    # AAAAE : 6
    # AAAAI : 7
    
    # (5*1) + 1
    # AAAA : 4
    # AAAE : 10
    # AAAI : 16

    # 5*((5*1) + 1) + 1
    # AAA : 3
    # AAE : 34
    # AAI : 65

    num = [781, 156, 31, 6, 1]
    answer = 0
    
    for i, w in enumerate(word):
        answer += alpha[w] * num[i] + 1
    
    return answer