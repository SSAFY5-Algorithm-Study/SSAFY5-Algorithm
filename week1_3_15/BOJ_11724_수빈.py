'''
11724. 연결 요소의 개수
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
'''
# python 시간초과
# pypy로 하면 OK

def DFS(s):
    stack = [s]
    global cnt
    cnt += 1
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for n in AL[node]:
                if not visited[n]:
                    stack.append(n)


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

AL = [[] for _ in range(N+1)]
for u, v in edges:
    AL[u].append(v)
    AL[v].append(u)

cnt = 0
visited = [0] * (N + 1)

for i in range(1, N+1):
    # 방문하지 않은 경우에만 DFS 탐색 실행
    if not visited[i]:
        DFS(i)

print(cnt)

'''
[입력]
6 5
1 2
2 5
5 1
3 4
4 6

[출력]
2
'''