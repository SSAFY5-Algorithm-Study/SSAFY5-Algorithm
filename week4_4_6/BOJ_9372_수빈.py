'''
9372. 상근이의 여행

상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다. 
하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.
'''
# 트리로는 어떻게 풀지..?
import sys
input = sys.stdin.readline

def BFS(x):
    queue = [x]
    visited[x] = 1
    airplane = 0
    while queue:
        country = queue.pop(0)
        for c in AL[country]:
            if not visited[c]:
                visited[c] = 1
                airplane += 1
                queue.append(c)
    return airplane

# 테스트 케이스의 수
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    AL = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        start, end = map(int, input().split())
        # 왕복이므로 무방향
        AL[start].append(end)
        AL[end].append(start)
    
    print(BFS(1))

'''
[입력]
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

[출력]
2
4
'''