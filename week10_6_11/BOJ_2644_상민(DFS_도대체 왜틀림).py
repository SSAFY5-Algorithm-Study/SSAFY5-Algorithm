'''

아이디어
- 7이 3을 만날 수 있는 지 없는 지 파악
- 만날 수 있다면 횟수를 출력
- 없다면 -1 출력
- 서로의 관계를 타고 타고 가서 만날 수 있는지를 파악해야되기 때문에 DFS로 풀면될듯

'''


def DFS(start, end):
    visited[start] = 1
    if start == end:
        result[0] = result_temp[0]
        return
    for child in relations[start]:
        if not visited[child]:
            print(start, child)
            result_temp[0] += 1
            DFS(child, end)


N = int(input())
one, another = map(int, input().split())
M = int(input())
temp = list(tuple(map(int, input().split())) for _ in range(M))
relations = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for s, e in temp:
    relations[s].append(e)
    relations[e].append(s)
result = [-1]
result_temp = [0]
DFS(one, another)
print(result[0])