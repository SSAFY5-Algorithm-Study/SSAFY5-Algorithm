'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''
def DFS(x):
    # 들어온 놈 방문 체크
    visited[x] = 1
    # 들어온 놈과 연결된 놈들을 하나씩 꺼내서
    for i in AL[x]:
        # 만약 방문하지 않았으면 재귀
        if visited[i] == 0:
            DFS(i)
        
N, M = map(int, input().split())
AL = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    AL[s].append(e)
    AL[e].append(s)

visited = [0] * (N+1)
result = 0

for i in range(1, N+1):
    if visited[i] == 0:
        DFS(i)
        result += 1
print(result)