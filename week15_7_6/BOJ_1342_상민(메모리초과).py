'''
민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

아이디어
-> 모든 순열을 구하고 완전 탐색 해보자
'''

from itertools import permutations

s = input()
s_len = len(s)
s_permutations = set(permutations(s, len(s)))
ans = 0
for per in s_permutations:
    # flag = True
    standard = per[0]
    for i in range(1, s_len):
        if per[i] == standard:
            # flag = False
            break
        standard = per[i]
    else:
        ans += 1
print(ans)
    