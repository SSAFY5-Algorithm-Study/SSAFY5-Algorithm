
import sys
sys.stdin = open('input.txt')

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
                one_location.append((i, j, 0))
    if zero_count == 0:
        return 0


def BFS(ones):
    cnt = 0
    queue = ones
    # 토마토가 있는 지역에는 미리 발견 표시 해줌
    for y, x, z in queue:
        discovered[y][x] = 1
    while queue:
        cr, cc, cnt = queue.pop(0)
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if farm[nr][nc] == 0 and not discovered[nr][nc]:
                discovered[nr][nc] = 1
                queue.append((nr, nc, cnt + 1))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # -1로 padding
    farm = [[-1] + list(map(int, input().split())) + [-1] for _ in range(M)]
    farm.insert(0, [-1] * (N + 2))
    farm.append([-1] * (N + 2))
    one_location = []
    discovered = [[0] * (N + 2) for _ in range(M + 2)]
    if find_situations():
        print(find_situations())
    else:
        # BFS 시작
        print(BFS(one_location))