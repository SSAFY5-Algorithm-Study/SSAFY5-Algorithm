bonus_dict = {'S': 1, 'D': 2, 'T': 3, '0': 10}

def solution(dartResult):
    dartResult += '/'
    print(dartResult)
    result = [1] * 4
    s = 0
    for i in range(1, 4):
        # 점수가 10인지 아닌지 가려내기
        if dartResult[s+1] == '0':
            num = 10
            s += 1
        else:
            num = int(dartResult[s])
        # bonus 글자 알아내기
        bonus = bonus_dict[dartResult[s+1]]
        # 옵션 제외한 점수 계산하기
        score = num ** bonus
        
        # 옵션 유무에 따라 
        if dartResult[s+2] == '*':
            result[i] = score * 2
            result[i-1] *= 2
            s += 3
        elif dartResult[s+2] == '#':
            result[i] = score * (-1)
            s += 3
        else:
            result[i] = score
            s += 2
    
    answer = sum(result[1:4])
    return answer