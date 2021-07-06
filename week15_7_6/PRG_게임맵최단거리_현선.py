# 최단거리니까 BFS
# 쉽다 쉬워
def solution(maps):
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    def BFS():
        r = len(maps) - 1
        c = len(maps[0]) - 1
        q = [[0,0]]
        # 한칸 이동할때마다 visited 배열은 이전 칸 값 + 1로 저장.
        visited = [[0] * (c+1) for _ in range(r+1)]
        visited[0][0] = 1
        while q:
            cr,cc = q.pop(0)
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < r+1 and 0 <= nc < c+1 and maps[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append([nr,nc])
                    visited[nr][nc] = visited[cr][cc] + 1
                    # 목적지 도착하면 횟수 반환
                    if visited[r][c]:
                        return visited[r][c]
        # 목적지의 visited 값이 0이면 도착 못한다는 소리니까 -1 반환
        return -1
    answer = BFS()
    return answer