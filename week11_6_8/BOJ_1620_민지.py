import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

pokemons = [0]
for _ in range(N):
    pokemons.append(input())

for _ in range(M):
    target = input()
    print(pokemons.index(target) if target.isalpha() else pokemons[int(target)])
    

    # if target.isalpha():
    #     print(pokemons.index(target))
    # else:
    #     print(pokemons[int(target)])

