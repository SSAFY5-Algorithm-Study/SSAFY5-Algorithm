# 주변에 모두 -1인 0이나 1이 존재하면 -1을 출력
# 0이 없으면 0을 출력
# 1을 찾아야함
# 여러군데에서 동시에 출발하는 bfs 진행 필요

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_situations():
    zero_count = 0
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if farm[i][j] == 0:
                minus_count = 0
                zero_count += 1
                for r, c in dxy:
                    nr = i + r
                    nc = j + c
                    if farm[nr][nc] == -1:
                        minus_count += 1
                        if minus_count == 4:
                            return -1
            elif farm[i][j] == 1:
                one_location.append((i, j))
    if zero_count == 0:
        return 0


def BFS(sr, sc):
    queue = [(sr, sc)]
    while queue:
        r, c = queue.pop(0)




N, M = map(int, input().split())
farm = [[-1] + list(map(int, input().split())) + [-1] for _ in range(M)]
# padding
farm.insert(0, [-1] * (N + 2))
farm.append([-1] * (N + 2))
one_location = []
discovered = [[0] * (N + 2) for _ in range(M + 2)]
print(discovered)
for r, c in one_location:
    BFS(r, c)
