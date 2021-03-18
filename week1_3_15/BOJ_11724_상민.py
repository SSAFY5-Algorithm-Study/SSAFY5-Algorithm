import sys
sys.stdin = open('input.txt')


def DFS(vertex):
    # 방문 표시
    visited[vertex] = 1
    for near in connected[vertex]:
        if not visited[near]:
            DFS(near)



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # 1부터 세어주기 위해서 N + 1
    connected = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for s, e in edges:
        connected[s] += [e]
        connected[e] += [s]
    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            DFS(i)
            cnt += 1
    print(cnt)