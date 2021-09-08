def solution(s):
    answer = []
    s = s.replace('{', '').replace('}}', '')
    s = s.split('},') 
    s.sort(key=len)
    # print(s)
    for i in range(len(s)):
        x = ''
        for j in range(len(s[i])):
            if s[i][j] != ',':
                x += s[i][j]
            else:
                y = int(x)
                if y not in answer:
                    answer.append(y)
                x = ''
        # print(x)
        if x and int(x) not in answer:
            answer.append(int(x))
    
    
    return answer