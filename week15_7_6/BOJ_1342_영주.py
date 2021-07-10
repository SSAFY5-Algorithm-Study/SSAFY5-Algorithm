# 1342. 행운의 문자열 (골드5)

from math import factorial


def permutation(depth, prev):
    if depth == length:
        lucky.add(''.join(case))
        return
    for i in range(length):
        if not check[i]:
            if s[i] == prev:
                continue
            case[depth] = s[i]
            check[i] = True
            permutation(depth+1, s[i])
            check[i] = False


s = input()
length = len(s)
if length == len(set(s)):
    print(factorial(length))
else:
    case = [0] * length # 순열로 나오는 각각의 경우
    check = [False] * length # 해당 문자를 뽑았는지 안뽑았는지 체크
    lucky = set()
    permutation(0, '')
    print(len(lucky))