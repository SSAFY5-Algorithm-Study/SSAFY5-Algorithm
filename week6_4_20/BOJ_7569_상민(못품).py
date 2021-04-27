import sys
sys.stdin = open('input.txt')

# 앞, 뒤, 상, 좌, 하, 우
dxy = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 0), (0, 0, 1)]


def find_one():
    zero_count = 0
    for i in range(H):
        for j in range(1, N + 1):
            for k in range(1, M + 1):
                if not box[i][j][k]:
                    zero_count += 1
                if box[i][j][k] == 1:
                    queue.append((i, j, k, 0))
    if not zero_count:
        return 0

def BFS():
    visited = [[[0] * (M + 2) for _ in range(N + 2)] for _ in range(H)]
    for a, b, c, cnt in queue:
        visited[a][b][c] = 1
    while queue:
        cz, cr, cc, cnt = queue.pop(0)
        print(cnt)
        error_cnt = 0
        for z, r, c in dxy:
            nz = cz + z
            nr = cr + r
            nc = cc + c
            if not visited[nz][nr][nc]:
                if not box[nz][nr][nc]:
                    queue.append((nz, nr, nc, cnt + 1))
                    box[nz][nr][nc] = 1
                    visited[nz][nr][nc] = 1
                elif box[nz][nr][nc] == -1:
                    error_cnt += 1
                    if error_cnt == 6:
                        return -1


T = int(input())
for tc in range(1, T + 1):
    M, N, H = map(int, input().split())
    box = [[[-1] * (M + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (M + 2)] for _ in range(H)]
    queue = []

    print(find_one())
    print(BFS())
