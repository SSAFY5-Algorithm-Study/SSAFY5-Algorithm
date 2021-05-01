def solution(dartResult):
    answer = []
    
    # S : 1제곱, D : 2제곱, T : 3제곱  ->   점수마다 하나씩 존대
    # * : 해당 점수 * 2, 직전 점수 * 2,  # : 해당 점수 * (-1)
    # * 가 첫번째에 나올 경우 : 해당 점수 * 2만
    # *와 # 중첩 가능.
    
    lst = list(dartResult)
    
    ############## 10 처리
    i = 1
    while i < len(lst):
        if lst[i] == '0' and lst[i-1] == '1':
            lst[i-1] += lst[i]
            lst.pop(i)
        i += 1
    
    ############## 계산
    no_num = {'S', 'D', 'T', '*', '#'}
    i = 0
    temp = 0
    while i < len(lst):
        if lst[i] not in no_num:
            temp = int(lst[i])
        else:
            if lst[i] == 'S':
                temp **= 1
                answer.append(temp)
            elif lst[i] == 'D':
                temp **= 2
                answer.append(temp)
            elif lst[i] == 'T':
                temp **= 3
                answer.append(temp)
            elif lst[i] == '*':
                temp = answer.pop()
                temp *= 2
                if len(answer) > 0:
                    pre = answer.pop()
                    pre *= 2
                    answer.append(pre)
                answer.append(temp)
            elif lst[i] == '#':
                temp = answer.pop()
                temp *= (-1)
                answer.append(temp)
        i += 1
    return sum(answer)