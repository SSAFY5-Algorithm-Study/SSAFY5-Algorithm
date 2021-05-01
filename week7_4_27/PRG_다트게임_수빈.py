calc = {
    'S': lambda x: x,
    'D': lambda x: x**2,
    'T': lambda x: x**3
}

def solution(dartResult):
    answer = 0
    
    # 10을 먼저 처리하고 시작
    i = 0
    dart = []
    while True:
        if i > len(dartResult) - 1:
            break
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            dart.append('10')
            i += 2
        else:
            dart.append(dartResult[i])
            i += 1
    
    temp = []
    for i in range(len(dart)):
        if dart[i].isdigit():
            num = int(dart[i])
            temp.append(calc[dart[i+1]](num))
        elif dart[i] == '*':
            if len(temp) == 1:
                temp[0] *= 2
            else:
                temp[-2] *= 2
                temp[-1] *= 2
        elif dart[i] == '#':
            temp[-1] *= (-1)

    return sum(temp)