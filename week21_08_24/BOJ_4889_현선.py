cnt = 1
while True:
    strings = list(input())
    if '-' in strings:
        break
    result = 0
    s = []
    for string in strings:
        if string == '{':
            s.append(string)
        # 닫는 괄호면 한 짝 완성.
        else:
            if s:
                s.pop(-1)
            # 근데 스택이 비어있다? 짝이 안맞으니 바꿔줘야지
            else:
                result += 1
                # }{ case
                s.append(string)
    # s = {{{{ 면 2번 바꿔야함. 즉, s의 길이를 2로 나눈 만큼 result에 더해줌.
    result += len(s) // 2
    print('{0}. {1}'.format(cnt, result))
    cnt += 1
    