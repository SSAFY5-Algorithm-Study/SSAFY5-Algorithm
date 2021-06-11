'''
https://programmers.co.kr/learn/courses/30/lessons/17684
'''
def solution(msg):
    alpha = {chr(i + 64): i for i in range(1, 27)}
    answer = []
    length = len(msg)
    number = 27
    i = 0
    j = 1
    
    while i < length and j <= length:
        w = msg[i:j]
        
        if alpha.get(w) != None:
            j += 1
            continue
        
        alpha[w] = number
        answer.append(alpha[msg[i:j-1]])
        number += 1
        i = j - 1

    answer.append(alpha[w])
    return answer