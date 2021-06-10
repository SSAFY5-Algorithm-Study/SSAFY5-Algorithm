# 1620. 나는야 포켓몬 마스터 이다솜 (실버4)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemons = [input().rstrip() for _ in range(n)]
book = dict(zip(pokemons, map(str, range(1, n+1))))
result = []
for _ in range(m):
    question = input().rstrip()
    if question.isdecimal():
        result.append(pokemons[int(question)-1])
    else:
        result.append(book[question])
print('\n'.join(result))