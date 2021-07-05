'''
14221. 편의점

영선이는 이사할 일이 생겨 집을 알아보고 있다. 영선이는 혼자 살기 때문에, 편의점에서 대충 때울 때가 많아, 
집을 고르는 기준을 편의점과의 거리가 가장 가까운 곳으로 하려한다.
영선이가 이사할 도시는 정점과 간선으로 표현할 수 있는데, 이사가려 하는 집의 후보들과 편의점은 정점들 위에 있다.
영선이는 캠프 강사 준비로 바쁘므로, 대신하여 집을 골라주자. 만약 거리가 같은 지점이 여러 개라면 정점 번호가 가장 낮은 곳으로 골라주자.

입력
처음 줄에는 정점의 개수 n, 간선의 개수 m이 주어진다.(2≤n≤5,000 , 1≤m≤100,000) 
다음 m줄에는 a,b,c가 주어지는데 이는 a,b를 잇는 간선의 거리가 c라는 것이다.( 1≤a,b≤n , 1≤c≤10,000)
다음 줄에는 집의 후보지의 개수 p와 편의점의 개수 q가 주어진다.( 2≤p+q≤n, 1≤p , 1≤q) 
다음 줄에는 집의 후보지들의 정점번호, 그 다음줄에는 편의점의 정점번호가 주어진다. 집의 후보지와 편의점은 서로 겹치지 않는다.

출력
편의점으로부터 가장 가까운 지점에 있는 집 후보의 정점 번호를 출력하시오. 
만약 거리가 같은 곳이 여러 군데라면 정점 번호가 낮은 곳을 출력하시오.
'''
# heapq 쓰는 이유
# https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC
# 다익스트라 설명
# https://brownbears.tistory.com/554

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start):
    queue = [(0, start)]
    distance = [987654321] * (n+1)
    distance[start] = 0
    
    while queue:    #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(queue)
        # 계산해 놓은 distance보다 현재 distance가 더 크면 볼 필요 없음
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node, w in graph[now]:
            cost = dist + w
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node]:
                distance[node] = cost
                # 다음 인접 거리 계산을 위해 큐에 삽입
                heappush(queue, (cost, node))
    return distance

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 집의 후보지 개수, 편의점 개수
p, q = map(int, input().split())

# 각각의 후보지 정점 번호
house = list(map(int, input().split()))
store = list(map(int, input().split()))

# 만약 거리가 같은 곳이 여러 군데라면 정점 번호가 낮은 곳을 출력하기 위해 정렬
house.sort()

min_d = 987654321
min_h = house[0]

for h in house:
    distance = dijkstra(h)
    for s in store:
        if distance[s] < min_d:
            min_h = h
            min_d = distance[s]

print(min_h)
'''
[입력]
6 9
1 4 1
1 5 2
1 6 3
2 4 2
2 5 3
2 6 1
3 4 3
3 5 1
3 6 2
3 3
1 2 3
4 5 6

[출력]
1
'''