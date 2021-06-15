'''
아이디어
- 포켓몬을 dictionary에 저장한다.
- 두 가지 방법
    { 번호 : 포켓몬 }
    { 포켓몬 : 번호 }

- dictionary는 in 연산자가 O(1) 시간밖에 걸리지 않기 때문에 빠를듯

'''


poketmon_dict = {}

N, M = map(int, input().split())
for i in range(1, N + 1):
    poketmon = input()
    poketmon_dict[str(i)] = poketmon
    poketmon_dict[poketmon] = i

for target in list(input() for _ in range(M)):
    print(poketmon_dict.get(target))
