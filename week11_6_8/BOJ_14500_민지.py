"""
H = 세로
W = 가로
"""
H, W = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]
print(arr)


# r, c 지점에서 시작했을때 가장 큰 합을 구하기
def find_max_sum(r, c):
    max_sum = 0
    # stack에 [row, col, 현재까지의 합, 현재까지 갯수, [방문한 점]] 을 저장한다
    stack = [[r, c, arr[r][c], 1, [(r, c)]]]
    while stack:
        cr, cc, temp_sum, cnt, visited = stack.pop(0)
        if cnt == 4:
            if temp_sum > max_sum:
                max_sum = temp_sum
            continue
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in visited:
                stack.append([nr, nc, temp_sum+arr[nr][nc], cnt+1, visited.append((nr, nc))])
    return max_sum
            

for r in range(H):
    for c in range(W):
        find_max_sum(r, c)