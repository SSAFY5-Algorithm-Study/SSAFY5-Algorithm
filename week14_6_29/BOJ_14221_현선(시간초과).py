'''
문제
영선이는 이사할 일이 생겨 집을 알아보고 있다. 영선이는 혼자 살기 때문에, 편의점에서 대충 때울 때가 많아, 
집을 고르는 기준을 편의점과의 거리가 가장 가까운 곳으로 하려한다.

영선이가 이사할 도시는 정점과 간선으로 표현할 수 있는데, 이사가려 하는 집의 후보들과 편의점은 정점들 위에 있다.

영선이는 캠프 강사 준비로 바쁘므로, 대신하여 집을 골라주자. 만약 거리가 같은 지점이 여러 개라면 정점 번호가 가장 낮은 곳으로 골라주자.

입력
처음 줄에는 정점의 개수 n, 간선의 개수 m이 주어진다.(2≤n≤5,000 , 1≤m≤100,000) 
다음 m줄에는 a,b,c가 주어지는데 이는 a,b를 잇는 간선의 거리가 c라는 것이다.( 1≤a,b≤n , 1≤c≤10,000)

다음 줄에는 집의 후보지의 개수 p와 편의점의 개수 q가 주어진다.( 2≤p+q≤n, 1≤p , 1≤q) 다음 줄에는 집의 후보지들의 정점번호, 
그 다음줄에는 편의점의 정점번호가 주어진다. 집의 후보지와 편의점은 서로 겹치지 않는다.

출력
편의점으로부터 가장 가까운 지점에 있는 집 후보의 정점 번호를 출력하시오. 만약 거리가 같은 곳이 여러 군데라면 정점 번호가 낮은 곳을 출력하시오.
'''

def djicstra(s,e):
    visited = [0] * (n+1)
    visited[s] = 1
    dist = [10000 * 100001] * (n+1)
    for jeongjum in gansun[s]:
        dist[jeongjum[0]] = jeongjum[1]
    i = 0 
    while i < n-1:
        minv = 10000 * 100001
        min_idx = 0
        for j in range(n+1):
            if visited[j] == 1:
                continue
            if dist[j] < minv:
                minv = dist[j]
                min_idx = j
        visited[min_idx] = 1
        for jeongjum in gansun[s]:
            dist[jeongjum[0]] = dist[jeongjum[0]] if dist[jeongjum[0]] < dist[min_idx] + jeongjum[1] else dist[min_idx] + jeongjum[1]
        i += 1
    return dist[e]
# n = 정점의 개수, m = 간선의 개수
# 최단거리 : 다익이
n, m = map(int,input().split())
gansun = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    gansun[a].append([b,c])
# p = 집 후보지 개수, q = 편의점 개수
p, q = map(int,input().split())
# 집 후보지, 편의점 후보지
house_candi = list(map(int,input().split()))
conve_candi = list(map(int,input().split()))


min_dist = 10000 * 100000 * 5001
min_house = 5001
for i in range(len(conve_candi)):
    for j in range(len(house_candi)):
        result = djicstra(conve_candi[i],house_candi[j])
        if result <= min_dist:
            min_dist = result
            if min_house > house_candi[j]:
                min_house = house_candi[j]
print(min_house)

