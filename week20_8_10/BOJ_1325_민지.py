"""
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다.
N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다.
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

변수
N = 컴퓨터의 갯수
M = 신뢰하는 연결의 갯수
AL = 컴퓨터들의 연결 고리 정보를 저장하는 이중 리스트
ex) AL[1] 에는 1번 컴퓨터를 해킹했을때 해킹할 수 있는 다른 컴퓨터들의 리스트가 저장되어있음
"""
from copy import deepcopy

N, M = map(int, input().split())
AL = [[] for _ in range(N+1)]
max_cnt = 0
max_nodes = []

for _ in range(M):
    A, B = map(int, input().split())
    AL[B].append(A)

# 시작점을 1~N까지로 설정해서 각각 DFS를 돈다
for s in range(1, N+1):
    visited = [0] * (N+1)
    visited[s] = 1
    stack = [s]
    cnt = 1
    # DFS 시작
    while stack:
        current = stack.pop()
        for i in AL[current]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                cnt += 1
    # 만약 cnt가 현재 나왔던 것들 중 max라면 max를 교체한다
    if cnt > max_cnt:
        max_cnt = cnt
        max_nodes = [s]
    elif cnt == max_cnt:
        max_nodes.append(s)

print(*max_nodes)