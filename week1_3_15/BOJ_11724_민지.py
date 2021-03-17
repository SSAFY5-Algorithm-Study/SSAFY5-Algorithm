# python으로 하면 시간초과
# pypy3로 했을때만 통과

import sys
sys.stdin = open('11724_input.txt', 'r')

N, M = map(int, input().split())

AL = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    AL[s].append(e)
    AL[e].append(s)

visited = [1] + [0]*N
nodes = 0
stack = []
# 방문 안한곳이 한곳이라도 있으면 반복
while 0 in visited:
    # 첫번째로 0이 나오는 곳 = visited 중에 방문 안한 첫번째 노드를 stack에 추가
    stack.append(visited.index(0))
    # 첫번째 노드를 기준으로 연결된 노드 전부 찾기: DFS
    while stack:
        cur = stack.pop()
        visited[cur] = 1
        for i in AL[cur]:
            if not visited[i]:
                stack.append(i)
    nodes += 1

print(nodes)