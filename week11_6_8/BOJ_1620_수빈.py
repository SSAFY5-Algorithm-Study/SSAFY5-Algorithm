'''
1620. 나는야 포켓몬 마스터 이다솜

https://www.acmicpc.net/problem/1620
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
monsters = {}
for i in range(1, N+1):
    monsters[input().rstrip()] = i

numbers = dict(map(reversed, monsters.items()))

for _ in range(M):
    problem = input().rstrip()

    if problem.isalpha():
        print(monsters[problem])
    else:
        print(numbers[int(problem)])

# N, M = map(int, input().split())
# monsters = [input() for _ in range(N)]
# mon_dict = { j: i for i, j in enumerate(monsters, 1) }
# numbers = dict(map(reversed, mon_dict.items()))

# for _ in range(M):
#     problem = input()
#     if problem.isalpha():
#         print(mon_dict[problem])
#     else:
#         print(numbers[int(problem)])

'''
[입력]
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

[출력]
Pikachu
26
Venusaur
16
14
'''