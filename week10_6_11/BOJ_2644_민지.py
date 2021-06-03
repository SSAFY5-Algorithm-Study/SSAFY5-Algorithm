import sys
sys.stdin = open('input.txt', 'r')


def calculate_chonsu(s):
    visited = [0] * N
    visited[s] = 1

    stack = [s]
    while stack:
        pass


# 사람 수
N = int(input())
# 촌수를 계산해야 되는 두 사람
A, B = map(int, input().split())
# 관계 수
M = int(input())

AL = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    AL[x].append(y)
    AL[y].append(x)

calculate_chonsu(A)