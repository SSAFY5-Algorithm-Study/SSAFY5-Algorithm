import sys
sys.stdin = open('input.txt')


def DFS(n, value):
    global max_value
    if n >= N and max_value < value:
        max_value = value
        return
    for i in range(n, N):
        DFS(i + 2, value + room[i][2])
    return max_value


N = int(input())
room = [tuple(map(int, input().split())) for _ in range(N)]
room.sort()
max_value = -987654321
# DFS
print(DFS(0, 0))