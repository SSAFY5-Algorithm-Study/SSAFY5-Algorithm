'''
13913. 숨바꼭질 4

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''
from collections import deque

def solve(visited, n, k):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            # 이동하는데 걸리는 최소시간
            print(visited[x])
            p = []
            # p에다가 마지막경로인 x를 넣고 x에다가 다시 path에 저장해둔 이전의 좌표 넣기
            # x가 시작점과 같아질때까지 반복
            while x != n:
                p.append(x)
                x = path[x]
            # while문이 n일때 끝나기 떄문에 n 추가
            p.append(n)
            p.reverse()
            print(*p)
            return
        for nx in (x+1, x-1, x*2):
            if 0<= nx <100001 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                #path[다음좌표]=현재좌표
                path[nx] = x
                queue.append(nx)

n, k = map(int, input().split())
visited = [0] * 100001
path = [0] * 100001
solve(visited, n, k)
'''
[입력]
5 17

[출력]
4
5 10 9 18 17
'''